bl_info = {
    "name": "SubmitWordPress",
    "author": "MITSUDA Tetsuo",
    "version": (0, 0, 4),
    "blender": (2, 6, 7),
    "location": "View3D > Tool Shelf > SubmitWordPress",
    "description": "submit your object on WordPress blog (using by XML-RPC)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}


# submitwordpress.py 0.03 by MITSUDA Tetsuo(Manda)
#
# submit your object on WordPress blog (using by XML-RPC)
#
# if you put romakanatbl.py on ${addonpath}/romakanatbl/ ,
# you can use roma-ji extention.
# (in title and text )some uppercase alphabet will be Japanese hiragana :)

import bpy
import os
import xmlrpc.client
import time

kanaflg = False

# import romankanatbl as extention
try:
    import romakanatbl.romakanatbl as rk
    kanaflg = True
    print("[SubmitWordPress] romankana extention is available.")
except:
    print("[SubmitWordPress] no romankana extention.")

# save an openGL render
def create_image(imgsel):
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
    if imgsel == "opengl":
        filepath += ".jpg"
        bpy.ops.render.opengl(write_still=True, view_context=True)
    elif imgsel == "screenshot":
        filepath += ".png"
        bpy.ops.screen.screenshot(filepath=filepath, 
                                  check_existing=False,
                                  full=True)

    
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
    size = os.path.getsize(filepath)

    return(filepath)

# read config from the file
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
    else:
        print("[SubmitWordPress] can't read configuration. please update your info.")

    return((user,passwd,urlstr))

class DialogOperator(bpy.types.Operator):
    bl_idname = "object.dialog_operator"
    bl_label = "Information"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text=bpy.context.scene.wpdialog_message)


# submit it!
class SubmitWordPressOperator(bpy.types.Operator):

    bl_idname = "wm.submitwordpressope"
    bl_label = "SubmitWordPress"
    
    def getkana(self,line):
        ht = rk.RomaKanaTable()
        ht.init()
        ht.makeTable(rk.ROMANHIRAGANATABLE,rk.ROMANHIRAGANATABLE_NASAL,
                 rk.ROMANHIRAGANA_GEMINATECONSOANT,rk.HIRAGANA_GEMINATESTRING)
        return(ht.getkana(line,False))
    
    def execute(self, context):

        scene = bpy.context.scene
        
        user = scene.wppanel_user
        passwd = scene.wppanel_passwd
        passwdhidden = scene.wppanel_passwdhidden
        urlstr = scene.wppanel_urlstr
        pubflg = scene.wppanel_pubflg
        title = scene.wppanel_title
        text = scene.wppanel_text
        imgsel = scene.wppanel_imgsel
        imgstr = ""
        mimetype = "image/jpeg"

        
        if passwd != "":
           passwdhidden = passwd

        #for test
        test = False

        if test:
            print("user:     " + user )
            print("title:    " + title )
            print("pwdhidden:" + passwdhidden )
        else:
            
            server = xmlrpc.client.ServerProxy(urlstr)

            blog_id = "blog"
            
            # post OpenGL image ( not delete the image. )
            if imgsel != 'noimage':
            
                filepath = create_image(imgsel)

                file=open(filepath,"rb")
                file_enc=xmlrpc.client.Binary(file.read())
                file.close()

                # set mimetype
                ext = os.path.splitext(filepath)
                if ext[1] == ".jpg":
                    mimetype = "image/jpeg"
                elif ext[1] == ".png":
                    mimetype = "image/png"
                
                image_content={'name':filepath,'type':mimetype,'bits':file_enc,'overwrite':True}

                # upload
                result=server.wp.uploadFile(blog_id, user, passwdhidden, image_content)
                imgurl = result.get("url")
                
                imgstr = "<p><img src = \""+ imgurl + "\"></p>\n"


            # title : UPPERCASE alphabet (roma-ji) will convert Japanese kana
            if scene.wppanel_titleflg :
                title = self.getkana(title)

            # text : UPPERCASE alphabet (roma-ji) will convert Japanese kana
            if scene.wppanel_textflg :
                text = self.getkana(text)

            content = "<p>"+ text + "</p>\n"+ imgstr + \
            "<p>This post is submitted from SubmitWordPress Add-on on Blender" + \
            bpy.app.version_string + "</p>"

            blog_content = { 'title' : title, 'description' : content }

            post_id = int(server.metaWeblog.newPost(blog_id, user, passwdhidden, blog_content,0))
        
            if pubflg :
                server.mt.publishPost(post_id, user, passwdhidden)
            
            scene.wpdialog_message = "finished."
            bpy.ops.object.dialog_operator('INVOKE_DEFAULT')


        return {'FINISHED'}

# update your account information
class UpdateAccountOperator(bpy.types.Operator):

    bl_idname = "wm.updateaccountope"
    bl_label = "Update"

    def execute(self, context):

        scene = bpy.context.scene
        user = scene.wppanel_user
        passwd = scene.wppanel_passwd
        urlstr = scene.wppanel_urlstr
        
        if passwd != "":
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
        
            scene.wppanel_passwdhidden = passwd
            scene.wppanel_passwd = ""
            scene.wpdialog_message = "update is done."
        
        else:
            scene.wpdialog_message = "password is empty. update is canceled."

        bpy.ops.object.dialog_operator('INVOKE_DEFAULT')

        return {'FINISHED'}
    
# restore your account information from the file
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
        scene.wppanel_passwd = ""
        scene.wppanel_passwdhidden = passwd 
        scene.wppanel_urlstr = urlstr

        scene.wpdialog_message = "restore is done."
        bpy.ops.object.dialog_operator('INVOKE_DEFAULT')

        return {'FINISHED'}

# Panel 
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
        
        if scene.wppanel_kanaflg :
            row.prop(scene, "wppanel_titleflg")
            row = layout.row()
        
        
        row.prop(scene, "wppanel_text")
        row = layout.row()
        
        if scene.wppanel_kanaflg :
            row.prop(scene, "wppanel_textflg")
            row = layout.row()
        
        row.prop(scene, "wppanel_imgsel")
        row = layout.row()
        row.operator("wm.submitwordpressope")


def register():
    bpy.utils.register_class(SubmitWordPressOperator)
    bpy.utils.register_class(UpdateAccountOperator)
    bpy.utils.register_class(RestoreAccountOperator)
    bpy.utils.register_class(VIEW3D_PT_SubmitWordPressPanel)
    bpy.utils.register_class(DialogOperator)
    
    user = ""
    passwd = ""
    urlstr =""
    
    (user,passwd,urlstr)=readconfig()

    bpy.types.Scene.wppanel_user = bpy.props.StringProperty(name="user", default = user )
    bpy.types.Scene.wppanel_passwd = bpy.props.StringProperty(name="password", default = '')
    bpy.types.Scene.wppanel_passwdhidden = bpy.props.StringProperty(name="password", default = passwd)
    bpy.types.Scene.wppanel_urlstr = bpy.props.StringProperty(name="url", default = urlstr)
    bpy.types.Scene.wppanel_pubflg = bpy.props.BoolProperty(name="publish", default = False )
    bpy.types.Scene.wppanel_title = bpy.props.StringProperty(name="title", default = '' )
    bpy.types.Scene.wppanel_text = bpy.props.StringProperty(name="text", default = '')
    bpy.types.Scene.wppanel_imgsel = bpy.props.EnumProperty(name="images",
                                     items = (('opengl', "OpenGL preview", "with OpenGL preview"),
                                     ('screenshot', "Screenshot", "take Screenshot"),
                                     ('noimage', "no image", "no image")),default = 'opengl')

    bpy.types.Scene.wppanel_kanaflg = bpy.props.BoolProperty(name="usekana", default = kanaflg )
    bpy.types.Scene.wppanel_titleflg = bpy.props.BoolProperty(name="title is roman-kana", default = kanaflg )
    bpy.types.Scene.wppanel_textflg = bpy.props.BoolProperty(name="text is roman-kana", default = kanaflg )

    bpy.types.Scene.wpdialog_message = bpy.props.StringProperty(name="message", default = '<message>')


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_SubmitWordPressPanel)
    bpy.utils.unregister_class(SubmitWordPressOperator)
    bpy.utils.unregister_class(UpdateAccountOperator)
    bpy.utils.unregister_class(RestoreAccountOperator)
    bpy.utils.unregister_class(DialogOperator)

    del bpy.types.Scene.wppanel_user
    del bpy.types.Scene.wppanel_passwd
    del bpy.types.Scene.wppanel_passwdhidden
    del bpy.types.Scene.wppanel_urlstr
    del bpy.types.Scene.wppanel_pubflg
    del bpy.types.Scene.wppanel_title
    del bpy.types.Scene.wppanel_text
    del bpy.types.Scene.wppanel_imgsel

    del bpy.types.Scene.wppanel_kanaflg
    del bpy.types.Scene.wppanel_titleflg
    del bpy.types.Scene.wppanel_textflg

    del bpy.types.Scene.wpdialog_message

if __name__ == "__main__":
    register()

# Release log:
#    0.0.1    : Submit text title
#    0.0.2    : Submit text with OpenGL preview
#    0.0.3    : Submit text with ...
#                  OpenGL preview or Screen Shot
#               Do not display password at 'wppanel_passwd'
#               Roman-kana extention 
#                  put romakanatbl.py on ${addonpath}/romakanatbl/