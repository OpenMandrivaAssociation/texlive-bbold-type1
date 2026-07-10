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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The files offer an Adobe Type 1 format version of the 5pt, 7pt and 10pt
versions of the bbold fonts. The distribution also includes a map file,
for use when incorporating the fonts into TeX documents; the macros
provided with the original Metafont version of the font serve for the
scaleable version, too. The fonts were produced to be part of the TeX
distribution from Y&Y; they were generously donated to the TeX Users
Group when Y&Y closed its doors as a business.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/doc/fonts/bbold-type1
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/afm/public/bbold-type1
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bbold-type1
%dir %{_datadir}/texmf-dist/fonts/type1/public/bbold-type1
%doc %{_datadir}/texmf-dist/doc/fonts/bbold-type1/README
%doc %{_datadir}/texmf-dist/doc/fonts/bbold-type1/test.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bbold-type1/test.tex
%{_datadir}/texmf-dist/fonts/afm/public/bbold-type1/bbold10.afm
%{_datadir}/texmf-dist/fonts/afm/public/bbold-type1/bbold5.afm
%{_datadir}/texmf-dist/fonts/afm/public/bbold-type1/bbold7.afm
%{_datadir}/texmf-dist/fonts/map/dvips/bbold-type1/bbold.map
%{_datadir}/texmf-dist/fonts/type1/public/bbold-type1/bbold10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bbold-type1/bbold5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bbold-type1/bbold7.pfb
