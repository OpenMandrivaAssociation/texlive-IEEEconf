%global tl_name ieeeconf
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Macros for IEEE conference proceedings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/IEEEconf
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeeconf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeeconf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ieeeconf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The IEEEconf class implements the formatting dictated by the IEEE
Computer Society Press for conference proceedings.

