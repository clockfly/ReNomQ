### Command options
# default: Build a English document only(same as 'make html'). This is default.
# -transcript [ja, en]: This generates transcript files(po file) to _locale.
# -lang [ja, en, all]: This builds documentation for each languages.

# find rsts/api -type d -name autosum -print0 | xargs -0 rm -rf
CMDNAME=`basename $0`

help() {
  echo "Usage: $CMDNAME [-t (ja)] [-l (ja, en, all)]"
  echo ""
  echo "-t(ja)           This generates transcript files(po files)."
  echo "-l(en, ja, all)  This builds documentation."
}

build_as_lang() {
  if [ "$1" = "ja" ] || [ "$1" = "en" ]; then
    make -B -e SPHINXOPTS="-D language=$1" html
  elif [ "$1" = "all" ]; then
    rm -rf _build/html
    make -e SPHINXOPTS="-D language=ja" html
    mv _build/html _build/ja
    make html
    mv _build/ja _build/html
  else
    echo "Usage: $CMDNAME [-l (en, ja, all)]" 1>&2
    exit 1
  fi
}

build_transcript_of() {
  # According to the sphinx reference, `make gettext` generates pot files
  # to the _build/gettext directory. But actuary it will be placed to _build/locale.

  if [ ! -d _build/gettext ]; then
    mkdir _build/gettext
  fi

  if [ "$1" = "ja" ]; then
    make gettext
    sphinx-intl update -p _build/gettext -l ja
  else
    echo "Usage: $CMDNAME [-t (ja)]" 1>&2
    exit 1
  fi
}

if [ $# -lt 1 ]; then
  help
  exit 1
fi

while getopts ":tl-:" OPT
do
  case $OPT in
    "-" ) ;;
    "l" ) build_as_lang "$2";;
    "t" ) build_transcript_of "$2";;
     *  ) help;
          exit 1 ;;
  esac
done
exit 0
