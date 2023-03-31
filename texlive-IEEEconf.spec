Name:		texlive-ieeeconf
Version:	59665
Release:	4
Summary:	Macros for IEEE conference proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ieeeconf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeeconf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeeconf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeeconf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ieeeconf class implements the formatting dictated by the
IEEE Computer Society Press for conference proceedings.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ieeeconf
%doc %{_texmfdistdir}/doc/latex/ieeeconf
#- source
%doc %{_texmfdistdir}/source/latex/ieeeconf

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
