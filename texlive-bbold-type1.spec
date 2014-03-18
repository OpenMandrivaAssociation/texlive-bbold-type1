# revision 33143
# category Package
# catalog-ctan /fonts/bbold-type1
# catalog-date 2014-03-09 23:53:06 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-bbold-type1
Version:	20140309
Release:	1
Summary:	An Adobe Type 1 format version of the bbold font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bbold-type1
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold-type1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold-type1.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The files offer an Adobe Type 1 format version of the 5pt, 7pt
and 10pt versions of the bbold fonts. The distribution also
includes a map file, for use when incorporating the fonts into
TeX documents; the macros provided with the original Metafont
version of the font serve for the scaleable version, too. The
fonts were produced to be part of the TeX distribution from
Y&Y; they were generously donated to the TeX Users Group when
Y&Y closed its doors as a business.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/bbold-type1/bbold10.afm
%{_texmfdistdir}/fonts/afm/public/bbold-type1/bbold5.afm
%{_texmfdistdir}/fonts/afm/public/bbold-type1/bbold7.afm
%{_texmfdistdir}/fonts/map/dvips/bbold-type1/bbold.map
%{_texmfdistdir}/fonts/type1/public/bbold-type1/bbold10.pfb
%{_texmfdistdir}/fonts/type1/public/bbold-type1/bbold5.pfb
%{_texmfdistdir}/fonts/type1/public/bbold-type1/bbold7.pfb
%doc %{_texmfdistdir}/doc/fonts/bbold-type1/README
%doc %{_texmfdistdir}/doc/fonts/bbold-type1/test.pdf
%doc %{_texmfdistdir}/doc/fonts/bbold-type1/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
