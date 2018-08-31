:: Lint the whole App
@echo off
cls

pylint gnucash_portfolio_cli --output-format=colorized

pause

pylint test --output-format=colorized
