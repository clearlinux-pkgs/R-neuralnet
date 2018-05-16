#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-neuralnet
Version  : 1.33
Release  : 29
URL      : https://cran.r-project.org/src/contrib/neuralnet_1.33.tar.gz
Source0  : https://cran.r-project.org/src/contrib/neuralnet_1.33.tar.gz
Summary  : Training of Neural Networks
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
resilient backpropagation with (Riedmiller, 1994) or without
    weight backtracking (Riedmiller and Braun, 1993) or the
    modified globally convergent version by Anastasiadis et al.
    (2005). The package allows flexible settings through
    custom-choice of error and activation function. Furthermore,
    the calculation of generalized weights (Intrator O & Intrator
    N, 1993) is implemented.

%prep
%setup -q -c -n neuralnet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502413089

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502413089
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library neuralnet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library neuralnet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library neuralnet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/neuralnet/DESCRIPTION
/usr/lib64/R/library/neuralnet/INDEX
/usr/lib64/R/library/neuralnet/Meta/Rd.rds
/usr/lib64/R/library/neuralnet/Meta/features.rds
/usr/lib64/R/library/neuralnet/Meta/hsearch.rds
/usr/lib64/R/library/neuralnet/Meta/links.rds
/usr/lib64/R/library/neuralnet/Meta/nsInfo.rds
/usr/lib64/R/library/neuralnet/Meta/package.rds
/usr/lib64/R/library/neuralnet/NAMESPACE
/usr/lib64/R/library/neuralnet/R/neuralnet
/usr/lib64/R/library/neuralnet/R/neuralnet.rdb
/usr/lib64/R/library/neuralnet/R/neuralnet.rdx
/usr/lib64/R/library/neuralnet/help/AnIndex
/usr/lib64/R/library/neuralnet/help/aliases.rds
/usr/lib64/R/library/neuralnet/help/neuralnet.rdb
/usr/lib64/R/library/neuralnet/help/neuralnet.rdx
/usr/lib64/R/library/neuralnet/help/paths.rds
/usr/lib64/R/library/neuralnet/html/00Index.html
/usr/lib64/R/library/neuralnet/html/R.css
