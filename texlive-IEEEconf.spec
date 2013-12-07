# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/IEEEconf
# catalog-date 2009-04-06 20:17:45 +0200
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-IEEEconf
Version:	1.4
Release:	6
Summary:	Macros for IEEE conference proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/IEEEconf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEconf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEconf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEconf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The IEEEconf class implements the formatting dictated by the
IEEE Computer Society Press for conference proceedings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/IEEEconf/IEEEconf.cls
%doc %{_texmfdistdir}/doc/latex/IEEEconf/IEEEconf.pdf
%doc %{_texmfdistdir}/doc/latex/IEEEconf/README
#- source
%doc %{_texmfdistdir}/source/latex/IEEEconf/IEEEconf.dtx
%doc %{_texmfdistdir}/source/latex/IEEEconf/IEEEconf.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 752686
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 718694
- texlive-IEEEconf
- texlive-IEEEconf
- texlive-IEEEconf
- texlive-IEEEconf
- texlive-IEEEconf

