import customtkinter as ctk
from controllers import unblock_client, check_and_block, initialize_services

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GUI")
        self.geometry('800x500')

        # Initialize services
        self.api_service, self.blocker_service = initialize_services()

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        
        self.label = ctk.CTkLabel(master=self.frame, text="GUI")
        self.label.pack(pady=12, padx=10)

        self.block_button = ctk.CTkButton(master=self.frame, text="Block Client", command=self.block)
        self.block_button.pack(pady=10, padx=10)
        
        self.unblock_button = ctk.CTkButton(master=self.frame, text="Unblock Client", command=self.unblock)
        self.unblock_button.pack(pady=10, padx=10)

        #TODO change this label
        self.status_label = ctk.CTkLabel(master=self.frame, text="")
        self.status_label.pack(pady=12, padx=10)

    def block(self):
        print("Block client button pressed")
        try:
            check_and_block(self.api_service, self.blocker_service)
            self.status_label.configure(text="Client blocked successfully.")
        except Exception as e:
            print(f"An error occured while blocking: {e}")
    
    def unblock(self):
        print("Unblock client button pressed")
        try:
            unblock_client(self.blocker_service)
            self.status_label.configure(text="Client unblocked successfully.")
        except Exception as e:
            print(f"An error occured while unblocking: {e}")

    
app = MyApp()
app.mainloop()