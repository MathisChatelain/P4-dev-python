rm -rf flake-report
flake8 --format=html --htmldir=flake-report

sudo chown -R $USER:$USER .