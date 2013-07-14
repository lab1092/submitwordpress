bl_info = {
    "name": "SubmitWordPress",
    "author": "MITSUDA Tetsuo",
    "version": (0, 0, 2),
    "blender": (2, 6, 7),
    "location": "View3D > Tool Shelf > SubmitWordPress",
    "description": "submit your object on WordPress blog (using by XML-RPC)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}


import bpy
import os
import xmlrpc.client
import time

# save an openGL render
def create_image():
    # saving old settings
    old_path = bpy.context.scene.render.filepath
    old_fileformat = bpy.context.scene.render.image_settings.file_format
    old_extension = bpy.context.scene.render.use_file_extension
    old_x = bpy.context.scene.render.resolution_x
    old_y = bpy.context.scene.render.resolution_y
    old_percentage = bpy.context.scene.render.resolution_percentage
    old_aspect_x = bpy.context.scene.render.pixel_aspect_x
    old_aspect_y = bpy.context.scene.render.pixel_aspect_y
    
    # setting up render settings
    filepath = bpy.data.filepath
    filename_pos = len(bpy.path.basename(bpy.data.filepath))
    filepath = filepath[:-filename_pos]
    filename = time.strftime("Img%Y%m%d%H%M%S",
        time.localtime(time.time()))
    filepath += filename
    bpy.context.scene.render.filepath = filepath
    bpy.context.scene.render.image_settings.file_format = 'JPEG'
    bpy.context.scene.render.use_file_extension = True
    bpy.context.scene.render.resolution_x = 320
    bpy.context.scene.render.resolution_y = 240
    bpy.context.scene.render.resolution_percentage = 100
    bpy.context.scene.render.pixel_aspect_x = 1.0
    bpy.context.scene.render.pixel_aspect_y = 1.0
    
    # render
    bpy.ops.render.opengl(write_still=True, view_context=True)
    
    # restore old settings
    bpy.context.scene.render.filepath = old_path
    bpy.context.scene.render.image_settings.file_format = old_fileformat
    bpy.context.scene.render.use_file_extension = old_extension
    bpy.context.scene.render.resolution_x = old_x
    bpy.context.scene.render.resolution_y = old_y
    bpy.context.scene.render.resolution_percentage = old_percentage
    bpy.context.scene.render.pixel_aspect_x = old_aspect_x
    bpy.context.scene.render.pixel_aspect_y = old_aspect_y

    # return values
    filepath += ".jpg"
    size = os.path.getsize(filepath)

    return(filepath)


def readconfig():

    user = ""
    passwd = ""
    urlstr = ""
    token =""

    path = os.path.join(bpy.utils.user_resource('SCRIPTS'), "presets")
    filepath = os.path.join(path, "wpaccount.txt")
    if os.path.exists(filepath):
        file = open(filepath, 'r')
        token = file.read()
        file.close()

    elem = token.split("|")
    if len(elem) == 3:
        user = elem[0]
        passwd = elem[1]
        urlstr = elem[2]

    return((user,passwd,urlstr))


class SubmitWordPressOperator(bpy.types.Operator):

    bl_idname = "wm.submitwordpressope"
    bl_label = "SubmitWordPress"
    
    def execute(self, context):

        user = bpy.context.scene.wppanel_user
        passwd = bpy.context.scene.wppanel_passwd
        urlstr = bpy.context.scene.wppanel_urlstr
        pubflg = bpy.context.scene.wppanel_pubflg
        title = bpy.context.scene.wppanel_title
        text = bpy.context.scene.wppanel_text
        imgflg = bpy.context.scene.wppanel_imgflg
        imgstr = ""

        #test
        test = False
        
        if test:
            print("user:     " + user )
            print("title:    " + title )
        else:
            
            server = xmlrpc.client.ServerProxy(urlstr)

            blog_id = "blog"
            
            if imgflg:
            
                filepath = create_image()

                file=open(filepath,"rb")
                file_enc=xmlrpc.client.Binary(file.read())
                file.close()

                image_content={'name':filepath,'type':"image/jpeg",'bits':file_enc,'overwrite':True}

                result=server.wp.uploadFile(blog_id, user, passwd, image_content)
                imgurl = result.get("url")
                
                imgstr = "<p><img src = \""+ imgurl + "\"></p>\n"


            content = "<p>"+ text + "</p>\n"+ imgstr + \
            "<p>This post is submitted from SubmitWordPress Add-on on Blender" + \
            bpy.app.version_string + "</p>"

            blog_content = { 'title' : title, 'description' : content }

            post_id = int(server.metaWeblog.newPost(blog_id, user, passwd, blog_content,0))
        
            if pubflg :
                server.mt.publishPost(post_id, user, passwd)
            
            print("[SubmitWordPress]:submitted.")

        return {'FINISHED'}

class UpdateAccountOperator(bpy.types.Operator):

    bl_idname = "wm.updateaccountope"
    bl_label = "Update"

    def execute(self, context):

        user = bpy.context.scene.wppanel_user
        passwd = bpy.context.scene.wppanel_passwd
        urlstr = bpy.context.scene.wppanel_urlstr
        
        
        # store blog account info to file
        # [caution:the text is row ]
        token = user + "|" + passwd + "|" + urlstr
        
        path = os.path.join(bpy.utils.user_resource('SCRIPTS'), "presets")
        if not os.path.exists(path):
            os.makedirs(path)
        filepath = os.path.join(path, "wpaccount.txt")
        file = open(filepath, 'w+')
        file.write(token)
        file.close()
        
        return {'FINISHED'}
    
class RestoreAccountOperator(bpy.types.Operator):

    bl_idname = "wm.restoreaccountope"
    bl_label = "Restore"

    def execute(self, context):
        
        user = ""
        passwd = ""
        urlstr = ""
        (user,passwd,urlstr)=readconfig()

        scene = bpy.context.scene
        scene.wppanel_user = user
        scene.wppanel_passwd = passwd 
        scene.wppanel_urlstr = urlstr
        
        return {'FINISHED'}

class VIEW3D_PT_SubmitWordPressPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "Submit WordPress"
    bl_idname = "wm.submitwordpressprop"
    bl_options = {"DEFAULT_CLOSED"}


    def draw(self, context):
        layout = self.layout

        scene = bpy.context.scene
        
        row = layout.row()
        row.prop(scene, "wppanel_user")
        row = layout.row()
        row.prop(scene, "wppanel_passwd")
        row = layout.row()
        row.prop(scene, "wppanel_urlstr")

        col = layout.column(align=True)
        row = col.row()
        row.operator("wm.updateaccountope")
        row.operator("wm.restoreaccountope")
        
        row = layout.row()
        row.prop(scene, "wppanel_pubflg")
        row = layout.row()
        row.prop(scene, "wppanel_title")
        row = layout.row()
        row.prop(scene, "wppanel_text")
        row = layout.row()
        row.prop(scene, "wppanel_imgflg")
        row = layout.row()
        row.operator("wm.submitwordpressope")


def register():
    bpy.utils.register_class(SubmitWordPressOperator)
    bpy.utils.register_class(UpdateAccountOperator)
    bpy.utils.register_class(RestoreAccountOperator)
    bpy.utils.register_class(VIEW3D_PT_SubmitWordPressPanel)
    
    user = ""
    passwd = ""
    urlstr =""
    
    (user,passwd,urlstr)=readconfig()

    bpy.types.Scene.wppanel_user = bpy.props.StringProperty(name="user", default = user )
    bpy.types.Scene.wppanel_passwd = bpy.props.StringProperty(name="password", default = passwd)
    bpy.types.Scene.wppanel_urlstr = bpy.props.StringProperty(name="url", default = urlstr)
    bpy.types.Scene.wppanel_pubflg = bpy.props.BoolProperty(name="publish", default = False )
    bpy.types.Scene.wppanel_title = bpy.props.StringProperty(name="title", default = '' )
    bpy.types.Scene.wppanel_text = bpy.props.StringProperty(name="text", default = '')
    bpy.types.Scene.wppanel_imgflg = bpy.props.BoolProperty(name="OpenGL preview", default = True )


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_SubmitWordPressPanel)
    bpy.utils.unregister_class(SubmitWordPressOperator)
    bpy.utils.unregister_class(UpdateAccountOperator)
    bpy.utils.unregister_class(RestoreAccountOperator)
    del bpy.types.Scene.wppanel_user
    del bpy.types.Scene.wppanel_passwd
    del bpy.types.Scene.wppanel_urlstr
    del bpy.types.Scene.wppanel_pubflg
    del bpy.types.Scene.wppanel_title
    del bpy.types.Scene.wppanel_text
    del bpy.types.Scene.wppanel_imgflg


if __name__ == "__main__":
    register()
