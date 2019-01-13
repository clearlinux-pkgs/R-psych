#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-psych
Version  : 1.8.12
Release  : 20
URL      : https://cran.r-project.org/src/contrib/psych_1.8.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/psych_1.8.12.tar.gz
Summary  : Procedures for psychological, psychometric, and personality research.
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mnormt
BuildRequires : R-mnormt
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n psych

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547396652

%install
export SOURCE_DATE_EPOCH=1547396652
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psych
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psych
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psych
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

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
/usr/lib64/R/library/psych/NEWS.Rd
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
/usr/lib64/R/library/psych/doc/overview.R
/usr/lib64/R/library/psych/doc/overview.Rnw
/usr/lib64/R/library/psych/doc/overview.pdf
/usr/lib64/R/library/psych/doc/psych_for_sem.R
/usr/lib64/R/library/psych/doc/psych_for_sem.Rnw
/usr/lib64/R/library/psych/doc/psych_for_sem.pdf
/usr/lib64/R/library/psych/help/AnIndex
/usr/lib64/R/library/psych/help/aliases.rds
/usr/lib64/R/library/psych/help/paths.rds
/usr/lib64/R/library/psych/help/psych.rdb
/usr/lib64/R/library/psych/help/psych.rdx
/usr/lib64/R/library/psych/html/00Index.html
/usr/lib64/R/library/psych/html/R.css
