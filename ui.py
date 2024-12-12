from textual.app import App
from textual.widgets import Footer, Header, Button, Label, Placeholder, DataTable
from textual.containers import Grid, VerticalScroll, Container
from textual.screen import Screen


class MyApp(App):
    CSS_PATH = "main.tcss"

    BINDINGS = [
        ("a", "toggle_dark", "Toggle dark mode"),
        # ("q", "request_quit", "Quit"),
    ]

    def compose(self):
        yield Header()
        yield Footer()

    def on_mount(self):
        self.title = "Manage things"
        self.sub_title = "Da real sys admin app"
        # self.push_screen(WelcomePage("Welcome"))





import docker
dock = docker.from_env()

class WelcomePage(Screen):

    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.containersList = DataTable(id="containers-list", classes="containers-list")
        self.containersList.add_columns("id", "name", "status")


    def show_containers(self):
        for container in dock.containers.list():
            container = [
                    container.id,
                    container.name,
                    container.status, ]
            self.containersList.add_row(*container)
        

    def compose(self):
        self.show_containers()
        yield Header()
        yield Grid(
            # Label(self.message, id="title"),
            Button("Containers", variant="primary", id="containers"),
            Button("Images", variant="primary", id="images"),
            Button("Services", variant="default", id="services"),
            Button("Stacks", variant="default", id="stacks"),
            Button("Nodes", variant="default", id="nodes"),
            Container(
                self.containersList,
            ),

            id="question-dialog",
        )
        yield Footer()


    # def on_button_pressed(self, event):
    #     if event.button.id == "yes":
    #         self.dismiss(True)
    #     else:
    #         self.dismiss(False)
