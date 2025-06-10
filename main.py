
from db.database import get_connection
from ui.main_window import MainWindow

def main():
    app = MainWindow()
    conn = get_connection()
    # TODO: instantiate DAOs, Services, Controllers and inject into tabs
    app.mainloop()

if __name__ == "__main__":
    main()
