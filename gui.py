import os.path
from tkinter import *
import customtkinter
from main import OpenapiOPS


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.apikey = None
        self.title("OpenAPI ChatBot GUI")
        self.geometry(f"{800}x{400}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(30, 0), sticky="nsew")
        self.tabview.add("Operations")

        self.apikey_input_button = customtkinter.CTkButton(self.tabview.tab("Operations"), text="API KEY",
                                                           command=self.set_api_key)

        self.prompt_input_button = customtkinter.CTkButton(self.tabview.tab("Operations"), text="Message",
                                                           command=self.open_input_dialog_event)
        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Operations"), text='Clear',
                                                        command=self.sidebar_button_event)

        self.apikey_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.prompt_input_button.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.sidebar_button_1.grid(row=4, column=0, padx=50, pady=(10, 10))

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

    def set_api_key(self):
        import json

        if os.path.exists('data.json'):
            self.apikey_input_button.configure(state="disabled", text="Disabled API KEY")
            f = open('data.json')

            data = json.load(f)
            self.api_key = data['API_KEY']

        else:
            dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
            self.api_key = dialog.get_input()
            api_key_json = {'API_KEY': self.api_key}
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(api_key_json, f, ensure_ascii=False, indent=4)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        opapi = OpenapiOPS()
        opapi.api_key = self.api_key
        response = opapi.chat_prompt(message=dialog.get_input())
        self.textbox.insert("0.0", "\n")
        self.textbox.insert("0.0", response)
        self.textbox.insert("0.0", "\n" + "-----------------------------Finished--------------------------------------")

    def sidebar_button_event(self):
        self.textbox.delete("1.0", END)


if __name__ == "__main__":
    app = App()
    app.mainloop()