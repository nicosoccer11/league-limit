from controllers import unblock_client, check_and_block, initialize_services, load_user_data, save_user_data
import customtkinter as ctk

# Set appearance mode and color theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("blue")  # Changed to blue for a sleek look

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("League Client Blocker")
        self.geometry('500x400')  # Increased height for better spacing

        # Initialize services
        self.api_service, self.blocker_service = initialize_services()

        # Load saved user data if available
        user_data = load_user_data()
        self.username = user_data['username'] if user_data else ""
        self.tagline = user_data['tagline'] if user_data else ""
        self.path = user_data['path_to_client'] if user_data else ""

        # Main Frame for content
        self.frame = ctk.CTkFrame(master=self, corner_radius=15)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        # Main Title Label
        self.label = ctk.CTkLabel(master=self.frame, text="League Blocker", font=("Arial", 24, "bold"))
        self.label.pack(pady=20, padx=10)

        # Buttons with a modern look
        bold_font = ctk.CTkFont(size=16, weight="bold")

        # Block button
        self.block_button = ctk.CTkButton(master=self.frame, text="Block Client", 
                                          command=self.block, corner_radius=20, 
                                          font=bold_font, fg_color="#B90035",  # Custom color
                                          hover_color="#860026")  # Hover color
        self.block_button.pack(pady=15, padx=10)

        # Unblock button
        self.unblock_button = ctk.CTkButton(master=self.frame, text="Unblock Client", 
                                            command=self.unblock, corner_radius=20, 
                                            font=bold_font, fg_color="#29AA46",  # Custom color
                                            hover_color="#1F8135")
        self.unblock_button.pack(pady=15, padx=10)

        # Update User, Tagline, and PATH button (opens popup)
        self.update_button = ctk.CTkButton(master=self.frame, text="Set Username and PATH", 
                                           command=self.open_update_popup, corner_radius=20, 
                                           font=bold_font, fg_color="#17A2B8", hover_color="#138496")
        self.update_button.pack(pady=15, padx=10)

        # Status label with adjustable text
        self.status_label = ctk.CTkLabel(master=self.frame, text="", font=("Arial", 14))
        self.status_label.pack(pady=20, padx=10)

    def block(self):
        print("Block client button pressed")
        try:
            check_and_block(self.api_service, self.blocker_service)
            self.status_label.configure(text="Client blocked successfully.", text_color="green")
        except Exception as e:
            print(f"An error occurred while blocking: {e}")
            self.status_label.configure(text="Error blocking client.", text_color="red")
    
    def unblock(self):
        print("Unblock client button pressed")
        try:
            unblock_client(self.blocker_service)
            self.status_label.configure(text="Client unblocked successfully.", text_color="green")
        except Exception as e:
            print(f"An error occurred while unblocking: {e}")
            self.status_label.configure(text="Error unblocking client.", text_color="red")

    def open_update_popup(self):
        # Create a new window (popup)
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("Update Username and Tagline")
        self.popup.geometry("400x250")

        # Username entry in the popup
        self.popup_username_entry = ctk.CTkEntry(master=self.popup, placeholder_text="Username", font=("Arial", 14), )
        self.popup_username_entry.pack(pady=15, padx=20)

        # Tagline entry in the popup
        self.popup_tagline_entry = ctk.CTkEntry(master=self.popup, placeholder_text="Tagline", font=("Arial", 14))
        self.popup_tagline_entry.pack(pady=15, padx=20)

        # PATH entry in the popup
        self.popup_path_entry = ctk.CTkEntry(master=self.popup, placeholder_text="League Client PATH", font=("Arial", 14))
        self.popup_path_entry.pack(pady=15, padx=20)

        # Save button in the popup
        self.popup_save_button = ctk.CTkButton(master=self.popup, text="Save", 
                                               command=self.save_popup_data, corner_radius=15, 
                                               font=("Arial", 14, "bold"), fg_color="#FFC107")
        self.popup_save_button.pack(pady=20, padx=20)

    def save_popup_data(self):
        # Get the username and tagline from the popup entries
        username = self.popup_username_entry.get()
        tagline = self.popup_tagline_entry.get()
        path = self.popup_path_entry.get()

        # Save to JSON file
        save_user_data(username, tagline, path)

        # Update the main window's username and tagline
        self.username = username
        self.tagline = tagline
        self.path = path

        # Close the popup window
        self.popup.destroy()

        # Update status label
        self.status_label.configure(text="Username and PATH updated successfully.", text_color="blue")
        print(f"Saved: {username}, {tagline}, {path}")
