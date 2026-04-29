# Maintainer: uzki69 <uzakichan11224@gmail.com>
pkgname=make-jfnf
pkgver=1.0.0
pkgrel=1
pkgdesc="Make Jellyfin Name Format cli"
url="https://github.com/uzki69/MakeJFNF"
arch=('x86_64')
license=('custom')
depends=('python' 'coreutils')
options=(!strip)
source=("$pkgname-$pkgver.tar.gz::https://github.com/uzki69/MakeJFNF/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('f2981536ec03b250b779bf63a525de3df5bb2907783d437a7dc1f438c86628fa')

package() {
	install -D -m755 "${srcdir}/${pkgname}-${pkgver}/main.py" "${pkgdir}/usr/bin/jfnf"
	install -D -m644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"	
}
