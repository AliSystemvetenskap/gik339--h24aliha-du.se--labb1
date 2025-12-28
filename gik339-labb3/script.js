console.log("Uppgift 2 start");

console.log("Före blocket:");
console.log(typeof a, typeof b, typeof c); 

{
  var a = "Jag är var";
  let b = "Jag är let";
  const c = "Jag är const";

  console.log("Inuti blocket:");
  console.log(a);
  console.log(b);
  console.log(c);
}

console.log("Efter blocket:");
console.log(a); // funkar (var är inte block-scope)

console.log("Uppgift 2 slut");

/*
Reflektion uppgift 2:

1) var är inte block-scope utan funktions-scope. Därför är en variabel med var fortfarande
åtkomlig utanför ett { }-block.

let och const är block-scope. De finns bara inom blocket där de deklareras, så om man försöker
använda dem efter blocket får man ett ReferenceError.

2) console.log() fungerar bara där variabeln är i scope. Inuti blocket kan man skriva ut var/let/const.
Efter blocket kan man bara skriva ut var-variabeln, eftersom let och const inte existerar där.
*/

console.log("Uppgift 3 start");

console.log("'3' == 3:", "3" == 3);
console.log("'3' === 3:", "3" === 3);

console.log("NaN === NaN:", NaN === NaN);
console.log("Number.isNaN(NaN):", Number.isNaN(NaN));

console.log("null == undefined:", null == undefined);
console.log("null === undefined:", null === undefined);

const result = undefined ? "truthy" : "falsy";
console.log("undefined är:", result);

console.log("Uppgift 3 slut");

/*
Reflektion uppgift 3:

1) == gör typkonvertering (implicit konvertering) innan jämförelse. Därför blir '3' == 3 true,
för att strängen '3' konverteras till talet 3.
=== gör ingen typkonvertering och kräver både samma värde och samma typ, därför blir '3' === 3 false.

NaN är “Not a Number” och är ett speciellt värde som betyder att en matematisk operation misslyckats.
NaN är aldrig lika med något, inte ens sig själv, därför är NaN === NaN false. För att testa NaN
använder man t.ex. Number.isNaN().

null och undefined är olika typer, men med == behandlas de som “lika” i just det fallet, därför
är null == undefined true. Med === är de inte samma typ, därför är null === undefined false.

2) När ett uttryck står för sig självt i t.ex. en ternary eller if, så utvärderas det som truthy eller falsy.
undefined är falsy, därför väljs falsy-grenen i ternaryn.

3) undefined betyder att något saknar tilldelat värde (inte definierat).
null är ett medvetet “tomt” värde (man har satt det till inget).
NaN betyder att resultatet inte blev ett giltigt tal.
*/

console.log("Uppgift 4 start");

let name = "Ali";
console.log("Global name (före funktionen):", name);

function greet(name) {
  console.log("Inuti funktionen - parameter name:", name);
  return "Hej " + name;
}

const greeting = greet("Bilal");
console.log("Returvärde från greet():", greeting);

console.log("Global name (efter funktionsanrop):", name);

console.log("Uppgift 4 slut");

/*
Reflektion uppgift 4:

1) Funktionsdeklaration: function greet() { ... }
- Hoistas (kan anropas innan den står i koden).

Funktionsuttryck: const greet = function() { ... }
- Ligger i en variabel och hoistas inte på samma sätt, så man kan inte anropa innan den raden körts.

Arrowfunktion: const greet = () => { ... }
- Kortare syntax och fungerar som ett funktionsuttryck (behöver skapas innan den anropas).

Jag valde funktionsdeklaration eftersom den är tydlig och kan anropas oavsett var den ligger i filen.

2) Man måste tänka på var i koden man anropar funktioner.
Funktionsdeklarationer kan anropas innan de skrivs, men funktionsuttryck/arrowfunktioner
måste skapas först (annars får man fel).

3) Parametern name i greet(name) är en lokal variabel i funktionen och “skuggar” den globala variabeln name.
När jag skickar in greet("Mikaela") så blir parametern name = "Mikaela" i funktionen, men globala name
utanför funktionen är fortfarande "Ali". Om man ändrar den globala variabeln name påverkar det inte
parametern när man skickar in ett eget argument.

4) Parameter: variabeln i funktionsdefinitionen (t.ex. name i greet(name)).
Argument: värdet man skickar in vid anrop (t.ex. "Mikaela" i greet("Mikaela")).
Variabel: ett namn som pekar på ett värde i ett scope (t.ex. let name = "Ali").
*/
