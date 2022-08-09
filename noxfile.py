import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session()
def lint(session):
    """Performs pep8 and code formatting checks."""
    session.run('poetry', 'install')
    session.run('poetry', 'run', 'flake8')
    session.run('poetry', 'run', 'black', '.', '--check')


@nox.session(tags=['security'])
def bandit(session):
    """Performs code security checks."""
    session.run('poetry', 'install')
    session.run('poetry', 'run', 'bandit', 'quote.py')


@nox.session(tags=['security'])
def safety(session):
    """Checks vulnerabilities of the installed packages."""
    session.run('poetry', 'install')
    session.run('poetry', 'run', 'safety', 'check')


@nox.session()
def tests(session):
    """Run tests."""
    session.run('poetry', 'install')
    session.run('poetry', 'run', 'pytest')
