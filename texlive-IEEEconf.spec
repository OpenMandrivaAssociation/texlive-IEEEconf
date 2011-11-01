Name:		texlive-IEEEconf
Version:	1.4
Release:	1
Summary:	Macros for IEEE conference proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/IEEEconf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEconf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEconf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEconf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The IEEEconf class implements the formatting dictated by the
IEEE Computer Society Press for conference proceedings.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
