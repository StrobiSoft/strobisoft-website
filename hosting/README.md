# Saját szerveres próbakiadás

A három céges HTML-oldal és a CSS forrása a repóban van. A build Python 3-mal, csomagtelepítés nélkül fut. Az eredeti GitHub Pages beállítást az elkülönített ág megőrzi.

1. Futtasd a `python3 hosting/build.py /tmp/strobisoft-release` parancsot új célkönyvtárral. A manifest.json a public alkönyvtár összes kiszolgálható fájlját tartalmazza.
2. A broker jóváhagyott szállítási műveletével másold a teljes kiadást új, kizárólag adminisztrátor által írható releases/<manifest-sha256> könyvtárba. A digestet a szállítás előtt rögzítsd. Aktiválás előtt mentsd el az eredeti vhostokat, webgyökeret, jogosultságokat és az nginx -T kimenetét helyben, védett mentésbe.
3. A broker ellenőrzött kiadásválasztója a current hivatkozást atomikusan váltja át. Őrizd meg a régi kiadást és digestjét. Kezeletlen current könyvtárat ne írj felül. A céloldalhoz tartozó worker csak az engedélyezett webhely kiadásválasztóját írhatja.
4. A staging vhost kizárólag loopbacken figyel. A helyi portok ellenőrzése után nginx -t és szabályozott reload szükséges. Teszteld az összes manifestfájlt, a sitemapet, a robots.txt-t, a 404-et és a TLS-t a helyes hostnévvel. Az SSL-példa már létező tanúsítványt vár. Éles domainre kiadott tanúsítványt és internet felőli elérést külön kell igazolni.
5. Visszaállításkor válaszd az előző ellenőrzött digestet. Első telepítésnél a korábbi vhost és webgyökér mentése a visszaállítás alapja. Csak sikeres konfigurációteszt után töltsd újra az Nginxet. A tartalomváltás nem igényel DNS- vagy levelezési műveletet.

A HTML-fájlos Search Console-igazolás a céges főoldalhoz készült. Google a nyilvános domainen ellenőrzi. A NODE IJET önálló termékoldalának canonical címe külön tulajdon.
