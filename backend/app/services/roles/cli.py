import typer

app = typer.Typer()


@app.command()
async def get_roles():
    print("Hello world")


if __name__ == "main":
    app()
