%global tl_name bbold-type1
%global tl_revision 33143

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An Adobe Type 1 format version of the bbold font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bbold-type1
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The files offer an Adobe Type 1 format version of the 5pt, 7pt and 10pt
versions of the bbold fonts. The distribution also includes a map file,
for use when incorporating the fonts into TeX documents; the macros
provided with the original Metafont version of the font serve for the
scaleable version, too. The fonts were produced to be part of the TeX
distribution from Y&Y; they were generously donated to the TeX Users
Group when Y&Y closed its doors as a business.

