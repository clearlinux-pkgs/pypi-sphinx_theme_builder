#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-sphinx_theme_builder
Version  : 0.2.0b2
Release  : 13
URL      : https://files.pythonhosted.org/packages/95/5f/a9651c42b6a44633ef900d765e4235533e08d0ea1f1aa844f50a34e1537c/sphinx-theme-builder-0.2.0b2.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/5f/a9651c42b6a44633ef900d765e4235533e08d0ea1f1aa844f50a34e1537c/sphinx-theme-builder-0.2.0b2.tar.gz
Summary  : A tool for authoring Sphinx themes with a simple (opinionated) workflow.
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_theme_builder-bin = %{version}-%{release}
Requires: pypi-sphinx_theme_builder-license = %{version}-%{release}
Requires: pypi-sphinx_theme_builder-python = %{version}-%{release}
Requires: pypi-sphinx_theme_builder-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Sphinx Theme Builder
<!-- start-elevator-pitch -->
Streamline the Sphinx theme development workflow, by building upon existing
standardised tools.

%package bin
Summary: bin components for the pypi-sphinx_theme_builder package.
Group: Binaries
Requires: pypi-sphinx_theme_builder-license = %{version}-%{release}

%description bin
bin components for the pypi-sphinx_theme_builder package.


%package license
Summary: license components for the pypi-sphinx_theme_builder package.
Group: Default

%description license
license components for the pypi-sphinx_theme_builder package.


%package python
Summary: python components for the pypi-sphinx_theme_builder package.
Group: Default
Requires: pypi-sphinx_theme_builder-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_theme_builder package.


%package python3
Summary: python3 components for the pypi-sphinx_theme_builder package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_theme_builder)
Requires: pypi(nodeenv)
Requires: pypi(packaging)
Requires: pypi(pyproject_metadata)
Requires: pypi(rich)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-sphinx_theme_builder package.


%prep
%setup -q -n sphinx-theme-builder-0.2.0b2
cd %{_builddir}/sphinx-theme-builder-0.2.0b2
pushd ..
cp -a sphinx-theme-builder-0.2.0b2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680135908
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_theme_builder
cp %{_builddir}/sphinx-theme-builder-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_theme_builder/28fe1f46ac6435fe4c4fda18cd15499926faefd5 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stb

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_theme_builder/28fe1f46ac6435fe4c4fda18cd15499926faefd5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
