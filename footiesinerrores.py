from tkinter import*
import tkinter.messagebox as box

root = Tk()
root.title('Footie en pañales')
root.iconbitmap(default='C:\penguin.ico')
menu_bar = Menu(root)

#definiciones
def cut():
	content_text.event_generate('<<Cut>>')
	return 'break'
def copy():
	content_text.event_generate('<<Copy>>')
	return 'break'
def paste():
		content_text.event_generate('<<Paste>>')
		return 'break'
def undo():
	content_text.event_generate('<<Undo>>')
	return 'break'
def redo(event=None):
	content_text.event_generate('<<Redo>>')
	return 'break'
		
def select_all(event=None):
	content_text.tag_add('sel','1.0','end - 1 c')#rows start in 1 and columns in 0 so position at start is 1.0
	return 'break'

def find_text(event=None):
		search_toplevel=Toplevel(root)
		search_toplevel.title('Find Text')
		search_toplevel.transient(root)
		search_toplevel.resizable(False,False)
		Label(search_toplevel,text='Find All:').grid(row=0,column=0,sticky='e')
		search_entry_widget=Entry(search_toplevel,width=25)
		search_entry_widget.grid(row=0,column=1,padx=2,pady=2,sticky='we')
		search_entry_widget.focus_set()
		ignore_case_value=IntVar()
		Checkbutton(search_toplevel,text='Ignore Case',variable=ignore_case_value).grid(row=1,column=1,padx=2,pady=2,sticky='e')
		Button(search_toplevel,text='Find them!',underline=0,command=lambda: search_output(search_entry_widget.get(),
			ignore_case_value.get(),content_text,search_toplevel,
			search_entry_widget)).grid(row=0,column=2,sticky='e'+'w',padx=2,pady=2)
		def close_search_window():
			content_text.tag_remove('match','1.0',END)
			search_toplevel.destroy()
		search_toplevel.protocol('WM_DELETE_WINDOW',close_search_window)
		return 'break'
			
def search_output(pattern,if_ignore_case,content_text,search_toplevel,search_entry_widget):
	content_text.tag_remove('match','1.0',END)
	matches_found=0
	if pattern:
		start_pos='1.0'
		while True:
			start_pos=content_text.search(pattern,start_pos,nocase=if_ignore_case,stopindex=END)
			if not start_pos:
				break
			end_pos='{}+{}c'.format(start_pos,len(pattern))
			content_text.tag_add('match',start_pos,end_pos)
			matches_found+=1
			start_pos=end_pos
		content_text.tag_config('match',foreground='red',background='yellow')
	else:
		box.showwarning('No terms?','No terms to search.(Search Inbox Empty!)')
	
	search_toplevel.title('{} matches found'.format(matches_found))
	
	
		
#fin de definiciones		
new_file_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/new_file.gif')
open_file_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/open_file.gif')
save_file_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/save.gif')
undo_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/undo.gif')
redo_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/redo.gif')
cut_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/cut.gif')
copy_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/copy.gif')
paste_icon=PhotoImage(file='C:/my python scripts/footieicons/icons/paste.gif')

show_line_num=IntVar()
show_cursor_loc=IntVar()
highlight_current_line=BooleanVar()
theme_name=StringVar()

file_menu = Menu(menu_bar,tearoff=0)
#command no lleva comillas pero lo dejo asi para ver como queda(sino da error porque los comandos no estan definidos) 
file_menu.add_command(label='New',accelerator='Ctrl + N',compound='left',
                      image=new_file_icon,underline=0,command='new_file')
file_menu.add_command(label='Open',accelerator='Ctrl + O',compound='left',
                      image=open_file_icon,underline=0,command='open_file')
file_menu.add_command(label='Save',accelerator='Ctrl + S',compound='left',
                      image=save_file_icon,underline=0,command='save')
file_menu.add_command(label='Save as',accelerator='Shift + Ctrl + S',underline=2,command='save_as')
file_menu.add_separator()
file_menu.add_command(label='Exit',accelerator='Alt + F4',command='exit_editor')
	
edit_menu = Menu(menu_bar,tearoff=0)	

edit_menu.add_command(label='Undo',accelerator='Ctrl + Z',compound='left',image=undo_icon,command=undo)
edit_menu.add_command(label='Redo',accelerator='Ctrl + Y',compound='left',image=redo_icon,command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',accelerator='Ctrl + X',compound='left',image=cut_icon,command=cut)
edit_menu.add_command(label='Copy',accelerator='Ctrl + C',compound='left',image=copy_icon,command=copy)
edit_menu.add_command(label='Paste',accelerator='Ctrl + V',compound='left',image=paste_icon,command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find',accelerator='Ctrl + F',command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All',accelerator='Ctrl + A',underline=7,command=select_all)

view_menu = Menu(menu_bar,tearoff=0)
themes_menu=Menu(view_menu,tearoff=0)
themes_menu.add_radiobutton(label='Default',variable=theme_name)
view_menu.add_checkbutton(label='Show Line Number',variable=show_line_num)
view_menu.add_checkbutton(label='Show Cursor Location at Bottom',variable=show_cursor_loc)
view_menu.add_checkbutton(label='Highlight Current Line',variable=highlight_current_line)
view_menu.add_cascade(label='Themes',menu=themes_menu )

about_menu = Menu(menu_bar,tearoff=0)
about_menu.add_command(label='About',command='about_command')
about_menu.add_command(label='Help',accelerator='Shift + F1',command='help_command')

menu_bar.add_cascade(label='File',menu=file_menu)
menu_bar.add_cascade(label='Edit',menu=edit_menu)
menu_bar.add_cascade(label='View',menu=view_menu)
menu_bar.add_cascade(label='About',menu=about_menu)
root.config(menu=menu_bar)
#barra de shortcuts
shortcut_bar=Frame(root,height=25,bg='light sea green')
shortcut_bar.pack(expand='no',fill='x')
#barra de numero de linea
line_number_bar=Text(root,width=4, padx=3, takefocus=0,border=0,bg='khaki',state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')
#texto(principal) y scrollbar

content_text=Text(root,wrap='word',undo=True)
content_text.pack(expand='yes',fill='both')
#binding ctrl-y/Y for redo (mayusc y min sino no podria usarlo cuando bloq.may is on)
content_text.bind('<Control-y>',redo)
content_text.bind('<Control-Y>',redo)
#binding select all
content_text.bind('<Control-A>',select_all)
content_text.bind('<Control-a>',select_all)

scroll_bar=Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)#esta y la sig linea son las que conectan el texto con la barra y viceversa
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right',fill='y')

  
root.mainloop()
