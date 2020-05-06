from invoke import task


@task
def test(c, rebuild=False):
    # run unit tests in /tests dir
    c.run("python3.7 -m unittest discover test")