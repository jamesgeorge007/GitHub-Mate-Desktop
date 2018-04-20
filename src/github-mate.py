''' +-------------------------+
    | Authored by James George|  
    +-------------------------+ 
'''

from tkinter import *

class github_mate:

	  # Constructor which gets involed automatically when the github_mate class is instantiated.	

	  def __init__(self, master):

	  	master.title('GitHub-Mate')

	  	master.geometry('400x400')

	  	master.resizable(False, False)

	  	



if __name__ == '__main__':

    root = Tk()
    app = github_mate(root)	  	
