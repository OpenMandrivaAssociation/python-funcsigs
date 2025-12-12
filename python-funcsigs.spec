Summary:	Python function signatures
Name:		python-funcsigs
Version:	1.0.2
Release:	6
Group:		Development/Python
License:	BSD
Url:		https://pypi.python.org/pypi/funcsigs
Source0:	https://pypi.python.org/packages/94/4a/db842e7a0545de1cdb0439bb80e6e42dfe82aaeaadd4072f2263a4fbed23/funcsigs-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python2dist(setuptools)
BuildRequires:	python-distribute
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)

%description
funcsigs is a backport of the PEP 362 function
signature features from Python 3.3's inspect module.

%package -n python2-funcsigs
Summary:	Python function signatures
Group:		Development/Python
 
%description -n python2-funcsigs
funcsigs is a backport of the PEP 362 function
signature features from Python 3.3's inspect module.

%prep
%setup -q -c

mv funcsigs-%{version} python2
cp -r python2 python3

%build
pushd python2
python2 setup.py build
popd

pushd python3
python setup.py build
popd


%install
pushd python2
python2 setup.py install --skip-build --root %{buildroot}
popd

pushd python3
python setup.py install --skip-build --root %{buildroot}
popd

%files
%doc python3/LICENSE python3/CHANGELOG
%{py_puresitedir}/funcsigs/
%{py_puresitedir}/funcsigs*.egg-info*

%files -n python2-funcsigs
%doc python2/LICENSE python2/CHANGELOG
%{py2_puresitedir}/funcsigs/
%{py2_puresitedir}/funcsigs*.egg-info*
