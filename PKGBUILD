# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name guillou.gabriel@gmail.com
pkgname=vfio_deployer-git
pkgver=0.0.0
pkgrel=1
epoch=
pkgdesc="A KVM VFIO deployer from yaml"
arch=(x86_64)
url="https://github.com/pikatsuto/vfio_deployer.git"
license=('LGPL')
groups=()
depends=(virt-manager qemu vde2 ebtables iptables-nft nftables dnsmasq bridge-utils ovmf swtpm)
makedepends=(python python-pip python-setuptools pciutils)
checkdepends=()
optdepends=(linux-zen linux-zen-header computer-link)
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=(git+$url)
noextract=()
md5sums=('SKIP')
validpgpkeys=()

prepare() {
	cd "$pkgname-$pkgver"
	patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
}

build() {
	cd "$pkgname-$pkgver"
	./configure --prefix=/usr
	make
}

check() {
	cd "$pkgname-$pkgver"
	make -k check
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
