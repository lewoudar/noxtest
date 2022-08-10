import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session()
def lint(session):
    """Performs pep8 and code formatting checks."""
    session.install('poetry>=1.0.0,<2.0.0')
    session.run('poetry', 'install')
    session.run('flake8')
    session.run('black', '.', '--check')


@nox.session(tags=['security'])
def bandit(session):
    """Performs code security checks."""
    session.install('poetry>=1.0.0,<2.0.0')
    session.run('poetry', 'install')
    session.run('bandit', 'quote.py')


@nox.session(tags=['security'])
def safety(session):
    """Checks vulnerabilities of the installed packages."""
    session.install('poetry>=1.0.0,<2.0.0')
    session.run('poetry', 'install')
    session.run('safety', 'check')


@nox.session()
def tests(session):
    """Run tests."""
    session.install('poetry>=1.0.0,<2.0.0')
    session.run('poetry', 'install')
    session.run('pytest')
