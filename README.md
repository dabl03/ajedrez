# Ajedrez
[![logo de licencia MIT](https://user-images.githubusercontent.com/66857879/204139039-27024473-8c49-4240-b089-b6a42e7db8b4.png)](https://github.com/dabl03/ajedrez/blob/master/LICENSE)
<p>Juego del ajedrez creado en python usando pygame.</p>
<p>El ajedrez es un juego que se desarrolla sobre un tablero y que enfrenta a dos personas. Cada jugador cuenta con dieciséis piezas que puede desplazar, respetando ciertas reglas, sobre el tablero que está dividido en sesenta y cuatro casilleros, conocidos como escaques.</p>

## ¿Como jugarlo?

### Como usar la app?

<p>La apricacion es completamente grafica por lo que tienes que tocar una pieza y tocar la casilla a donde va a mover.</p>

### ¿Como jugar ajedrez?

<ul>
  <li>
    <b>Peon:</b> La pieza mas numero y mas importante en el ajedrez(Aunque tambien es la pieza de menor valor al momento de sacrificar). Cuando el peon no se ha movido ni una vez el puede mover dos casilla o una(Siendo desición del jugador) al frente. Cuando se ha movido solo se puede mover una casilla al frente. Cuando hay una pieza al frente el peon no se puede mover(Al menos que tenga una pieza enemiga y puedas comertela con ese peon), el peon come cuando hay una pieza enemiga en la casilla latero-superior. Y por ultimo cuando el peon llega al final de camino se transforma en cualquier pieza que quieras excepto el rey.
  </li>
  <li>
    <b>Torre:</b> Es una pieza de mucho valor(No tanto como la reina) que se puede mover en forma de cruz a cualquier casilla que quede dentro de esa cruz. El come cualquier pieza que este dentro de su camino, pero no puede traspasar ninguna pieza como si no existiera.
  </li>
  <li>
    <b>Afil:</b> Es una pieza de menor valor que la torre pero muy poderosa y util. Se mueve en forma de "X". Y come las pieza que estan en su camino
  </li>
  <li>
    <b>Caballo:</b> Es una pieza de igual valor que el afil y la mas fastidiosa para el enemigo(Despues de la reina). Se mueve en forma de saltos: dos casilla al frente y una a la derecha o izquierda, dos casilla detraz y una a la derecha o izquierda, dos casilla a la derecha y una al frente o atraz, y por ultimo se mueve dos casillas al la izquierda y una al frente o atraz. Come la pieza que esten en la casilla donde va a saltar.
  </li>
  <li>
    <b>Reina:</b> La pieza mas importante(Despues del rey por supuesto) con la que muchos lloran al perderla. Se mueve de forma de cruz y de forma de "X"(Se puede decir que es una combinación del afil y la torre). Come la pieza que esten en su camino.
  </li>
  <li>
    <b>El Rey:</b> La pieza mas importante de todo el ajedrez, tanto que si lo capturan se acaba el juego. Se mueve en cualquier dirección pero solo una casilla de esa dirección, no se puede mover a ninguna casilla que esté amenazada por una pieza enemiga. Come todo lo que este en su camino al menos que otra pieza lo este cuidando. El rey si lo amenazan las demas piezas no se pueden mover(Al menos que sea para protejerlo). Al morir se acaba la partida.
  </li>
</ul>

## Problemas:
- Las piezas no se acomodan al tamaño de la pantalla.
- las piezas no se pueden mover.
## Proxima Actualización
- Crearé una clase para los diferente tipos de piezas y sobreescribiré el como se mueven y como mueren
- Corregire los errores que acabo de mensionar.
- Reacomodaré el array de las piezas para que sean: Spawn:[Spawn(...), Spawn(...),...]
## Actualización
- Agregue soporte para redimensionamiento de pantalla(No tengo tiempo para arreglar el problema 1)
- Cree una clase para peon y ahora es posible que cada pieza tenga su imagenes sin necesidad de pasarsela por parametro al crear la clase
