# -*- coding: utf-8 -*-
"""
@author: Victor Barres

Defines the TCG_SCENE_BUILDER class that allows to create a TCG input scene.

Can be also be use in command line: python viewer.py
"""
class TCG_SCENE_BUILDER:
    """
    Sets up the TCG scene builder.
    
    Data:
        - server_port (INT): Server port value, default 8080.
        - builder_path (STR): Path to the scene builder.
        - data_path (STR): Path to the data folder (contains perceptual knowledge)
        - scene_path(STR): Path to the scenes folder from a given scene will be picked.
        - tmp (STR): Temp folder.
    """

    def __init__(self, data_path, scene_path, PORT=8080, builder_path="TCGSceneBuilder/"):
        """
        Requires the path (data_path) to the folder that contains the data to be diplayed in the viewer.
        """
        self.server_port = PORT
        self.builder_path = builder_path
        self.data_path = data_path
        self.scene_path = scene_path
        self.tmp = "tmp"
    
    def start_viewer(self):
        """
        Starts the viewer.
        """
        self._load_data()
        self._start_server()
        
    def _start_server(self):
        """
        Setting up server at port PORT serving the viewer folder defined by viewer_path
        and opens default browser to "http://localhost:PORT"
        """
        import os
        import SimpleHTTPServer
        import SocketServer
        
        import webbrowser
        PORT = self.server_port
    
        os.chdir(self.builder_path)
    
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    
        httpd = SocketServer.TCPServer(("", PORT), Handler)
    
        print "serving at port", PORT
        webbrowser.open_new("http://localhost:" + str(PORT))
        httpd.serve_forever()
        
    def _load_data(self):
        """
        Copies and creates all the required data in builder/tmp directory.
        """
        import os, shutil
        if os.path.exists(self.builder_path + self.tmp):
            shutil.rmtree(self.builder_path + self.tmp)
        print os.getcwd()
        shutil.copytree(self.data_path, self.builder_path + self.tmp + '/data/')
        shutil.copytree(self.scene_path, self.builder_path + self.tmp + '/scene/')

###############################################################################
if __name__ == '__main__':
    import os
    data_path = './data/'
    scene_folder = './scenes/'
    
    scene_list = os.listdir(scene_folder)
    print "Available scenes:\n"
    for s in scene_list:
        print "\t" + s
    
    filename = raw_input('Enter a file name: ')
    
    scene_path = scene_folder + filename
    
    mySceneBuilder= TCG_SCENE_BUILDER(data_path, scene_path)
    mySceneBuilder.start_viewer()
    
        
