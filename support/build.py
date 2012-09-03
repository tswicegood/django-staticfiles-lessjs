"""
Builds the version of Less.js that's in vendor/less.js and packages
it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "1.3.0"


def cp(src):
    cmd = [
        "cp -R vendor/less.js/%s lessjs/static/lessjs/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        'version': DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./lessjs/static/lessjs"], shell=True)
    cp("dist/less-%(version)s*.js*" % args)
    cp("LICENSE")

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
