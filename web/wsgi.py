from webapp import create_app

app = create_app()

if __name__ == "__main__":
    try:
        app.run()
    except Exception as ex:
        raise ex
