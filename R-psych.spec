#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-psych
Version  : 2.3.6
Release  : 69
URL      : https://cran.r-project.org/src/contrib/psych_2.3.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/psych_2.3.6.tar.gz
Summary  : Procedures for Psychological, Psychometric, and Personality
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mnormt
BuildRequires : R-mnormt
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n psych
pushd ..
cp -a psych buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687448448

%install
export SOURCE_DATE_EPOCH=1687448448
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/psych/CITATION
/usr/lib64/R/library/psych/DESCRIPTION
/usr/lib64/R/library/psych/INDEX
/usr/lib64/R/library/psych/Meta/Rd.rds
/usr/lib64/R/library/psych/Meta/data.rds
/usr/lib64/R/library/psych/Meta/features.rds
/usr/lib64/R/library/psych/Meta/hsearch.rds
/usr/lib64/R/library/psych/Meta/links.rds
/usr/lib64/R/library/psych/Meta/nsInfo.rds
/usr/lib64/R/library/psych/Meta/package.rds
/usr/lib64/R/library/psych/Meta/vignette.rds
/usr/lib64/R/library/psych/NAMESPACE
/usr/lib64/R/library/psych/News.Rd
/usr/lib64/R/library/psych/R/psych
/usr/lib64/R/library/psych/R/psych.rdb
/usr/lib64/R/library/psych/R/psych.rdx
/usr/lib64/R/library/psych/data/Rdata.rdb
/usr/lib64/R/library/psych/data/Rdata.rds
/usr/lib64/R/library/psych/data/Rdata.rdx
/usr/lib64/R/library/psych/doc/index.html
/usr/lib64/R/library/psych/doc/intro.R
/usr/lib64/R/library/psych/doc/intro.Rnw
/usr/lib64/R/library/psych/doc/intro.pdf
/usr/lib64/R/library/psych/doc/scoring.R
/usr/lib64/R/library/psych/doc/scoring.Rnw
/usr/lib64/R/library/psych/doc/scoring.pdf
/usr/lib64/R/library/psych/help/AnIndex
/usr/lib64/R/library/psych/help/aliases.rds
/usr/lib64/R/library/psych/help/paths.rds
/usr/lib64/R/library/psych/help/psych.rdb
/usr/lib64/R/library/psych/help/psych.rdx
/usr/lib64/R/library/psych/html/00Index.html
/usr/lib64/R/library/psych/html/R.css
