from invoke import task

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src ")
    ctx.run("coverage report -m ")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task(coverage_report)
def html(ctx):
    ctx.run("google-chrome htmlcov/index.html")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")


@task
def start(ctx):
    ctx.run("python3 src/main.py")

@task
def  tui(ctx):
    ctx.run("python3 src/main_tui.py")