Quran Images
============

This project contains tools to convert images of the Holy Quran pages from
[King Fahd Glorious Quran Printing Complex](http://www.qurancomplex.org/) to
a format that I would like to use. In this case, from a full page in Adobe
Illustrator's format to a cropped page version in SVG and PNG formats.

Sources
-------

Raw images are from <http://dm.qurancomplex.gov.sa/hafsdownload/>


Requirements
------------

To run the conversion tools, the following additional tools are required.

* Inkscape
* Unzip
* Python 3

To run the tools in a headless server (e.g. VPS), install the following
(Ubuntu) packages:

* xserver-xorg-video-dummy
* vnc4server


Conversion
----------

Commands to convert the images

    # apt-get install xserver-xorg-video-dummy vnc4server inkscape unzip python3 --no-install-recommends
    # vncserver :0
    # wget http://download.qurancomplex.gov.sa/dm/hafs/hafs1422_ai_v1.0.zip
    # export DISPLAY=:0
    # ./tools/convert-all.sh hafs1422_ai_v1.0.zip

