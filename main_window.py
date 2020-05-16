from gui_filter_window import Ui_MainWindow as main_gui
from gui_spell_dialog import Ui_Dialog as spell_gui

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QWidget
from PyQt5 import QtCore, QtGui

"""
A GUI for searching through the DnD 5E spell list! 
"""

import sys, httplib2, os
import json

class SpellItem(QtGui.QStandardItem):
    """
    These are the items added to the great big list of spells. 

    Each carries an attribute ("this_path"), that specifies which json file correlates with this entry
    """

    def __init__(self, value, this_path):
        super(SpellItem,self).__init__(value)
        self._this_path = this_path

    @property
    def path(self):
        return(self._this_path)

class main_window(QMainWindow):
    """
    The main filter window
    """

    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.ui = main_gui()
        self.ui.setupUi(self)

        # which api to use
        # create a machine for Interneting 
        self.addr = 'http://www.dnd5eapi.co'
        self.http = httplib2.Http()
        
        # make sure the master spell list is there, download if it isn't
        self.datadir = os.path.join(os.path.dirname(__file__), "data")
        self.spell_list = os.path.join( self.datadir, "master.json")
        self.check_spell_list()

        # set up the menu with all the spell results
        self.ui.spell_list_entry = QtGui.QStandardItemModel()
        self.ui.listView.setModel( self.ui.spell_list_entry )
        self.ui.listView.clicked[QtCore.QModelIndex].connect( self.spell_item_clicked )

        # update the gui whenever an entry is changed
        self.ui.comboBox.currentIndexChanged.connect( self.update )
        self.ui.comboBox_2.currentIndexChanged.connect( self.update )
        self.ui.lineEdit.textChanged.connect(self.update)
        self.ui.check_name.stateChanged.connect(self.update)
        self.ui.check_desc.stateChanged.connect(self.update)

        # load in all the spells! 
        self.ui.check_name.setChecked(True)
        self.update()

    def get_number_append(self, number):
        """
        So, like, this takes a stringized number

        And it returns the letters at the end... so, like, 1st 2nd 3rd etc... 
        """
        last = number[-1]
        if last=='1':
            return('st')
        if last=='2':
            return('nd')
        if last=='3':
            return('rd')
        else:
            return('th')

    def spell_item_clicked(self, index):
        """
        This is called whenever a spell is clicked. It opens up the spell dialog and sets the relevant values to how they should be! 
        """
        item = self.ui.spell_list_entry.itemFromIndex( index )
        where = item.path

        f = open(where)
        data = json.load(f)
        f.close()

        dialog = spell_dialog(self)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose )
        
        dialog.ui.label.setText( data["name"] )
        fancy = str(data['level'])
        fancy += self.get_number_append(fancy)
        fancy += " level "+data['school']['name']
        dialog.ui.label_2.setText(fancy)
        
        dialog.ui.casting_time_val.setText(data['casting_time'])
        dialog.ui.range_text.setText(data['range'])
        
        comp = ""
        for compo in data['components']:
            comp+=compo+" "
        if 'material' in data:
            comp+= ": " +data['material']

        dialog.ui.comp_text.setText(comp)
        dialog.ui.dur_text.setText(data['duration'])
        
        classes_block = ""
        for i in data['classes']:
            if classes_block!='':
                classes_block+=", "
            classes_block+= i['name']
        dialog.ui.class_text.setText(classes_block)
        dialog.ui.textBrowser.setText(" ".join(data['desc']))

        dialog.exec_()


    def check_spell_list(self):
        """
        Verifies that there is a local copy of the master spell list 
        """

        # make sure the data directory exists 
        if os.path.exists(self.datadir):
            pass
        else:
            os.mkdir(self.datadir)

        if os.path.isfile( self.spell_list ):
            # file is already there, so that's good 
            # TODO: check if file is gucci 
            pass
        else:
            # download and write the json file 
            content = self.http.request( self.addr + "/api/spells" )
            f = open( self.spell_list, 'wb')
            f.write(content[1])
            f.close()

    def check_spell(self, api_url):
        """
        Checks if the spell for that api_url is there
        Downloads it if not 
        """
        file_name = "spell_" + api_url.split("/")[-1] +".json"
        full_path = os.path.join( self.datadir, file_name)

        if not os.path.isfile( full_path ):
            f = open( full_path, 'wb')
            content = self.http.request( self.addr + api_url )
            f.write(content[1])
            f.close()

        return(full_path)


    def satisfies(self, spell_fl):
        """
        Checks whether the json-spell-entry satisfies the current filters

        spell_fl is a very specifically formated dicitonary as loaded by json from the spell files 
        """
        level = str(spell_fl['level'])
        casting = [ i['name'] for i in spell_fl['classes'] ]
        
        search = self.ui.lineEdit.text().lower()

        if not (search==""):
            # check if what's there matche
            if self.ui.check_name.isChecked():
                sat_name = search in spell_fl['name'].lower()
            else:
                sat_name = False
            if self.ui.check_desc.isChecked():
                sat_desc = search in (" ".join(spell_fl['desc'])).lower()
            else:
                sat_desc = False

            if not (sat_name or sat_desc):
                return(False)

        if not( self.ui.comboBox.currentText()=="Any" or self.ui.comboBox.currentText() in casting ):
            return(False)
        if not( self.ui.comboBox_2.currentText()=="Any" or self.ui.comboBox_2.currentText()==level):
            return(False)
        return(True)


    def update(self):
        """
        Called whenever the filters have changed and we need to load up a new list of spells 
        """
                        
        # pass over master spell list
        self.check_spell_list()
        f = open( self.spell_list, 'r')
        master_list = json.load(f)
        f.close()
        
        # clear the list of spells in the list 
        self.ui.spell_list_entry.clear()

        # go over all the spells in the master list 
        for entry in master_list['results']:
            # make sure the spell we're iterating over has a correlating data file, get its location
            path = self.check_spell( entry['url'])
            f = open(path,'r')
            data = json.load(f)
            f.close()

            # if it satisfies the filters, add it to the shown list 
            if self.satisfies(data):
                # add it to the thing
                self.ui.spell_list_entry.appendRow(SpellItem(entry['name'],path))

        

class spell_dialog(QDialog):
    """
    Very basic little dialog box for the spells when you click on them
    """
    def __init__(self,parent):
        super(spell_dialog,self).__init__(parent)
        self.ui = spell_gui()
        self.ui.setupUi(self)


# launch the app
app = QApplication(sys.argv)
app_instance = main_window()
if __name__=="__main__":
    app_instance.show()
    sys.exit(app.exec_())
