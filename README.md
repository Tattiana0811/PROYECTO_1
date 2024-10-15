## PRIMER PROYECTO

### Oscilaciones en un Circuito RLC.

Los circuitos RLC ofrecen unas propiedades oscilatorias, ya que, están compuestos por resistencias (R), bobinas que producen inductancia (L) y capacitores (C), exhiben una variedad de resultados dinámicos cuando se tiene una fuente de entrada. Estos circuitos varían según los valores de los componentes y la frecuencia de la señal de entrada. Produciendo diferentes formas de oscilar, desde oscilaciones amortiguadas hasta críticamente amortiguadas.

En un circuito LC, la energía está en constante intercambio entre el inductor y el capacitor, lo que da lugar a un comportamiento de oscilación que no desaparece. Sin embargo, al agregar una resistencia R al circuito, la energía comienza a disiparse como calor; dependiendo del valor de R, el sistema puede comportarse de distintas maneras:
1.	**Subamortiguado**: $R<2\sqrt \frac {L}{C}$. Son aquellos sistemas donde el circuito oscila, pero su amplitud decrece con el tiempo.
2.	**Críticamente amortiguado**: $R=2\sqrt \frac {L}{C}$. Son dichos sistemas donde el circuito alcanza el equilibrio más rápido sin oscilar.
3.	**Sobreamortiguado**: $R>2\sqrt \frac {L}{C}$. Sucede cuando los circuitos no oscilan y la corriente disminuye exponencialmente sin oscilaciones de por medio. 
La relación entre ambos circuitos LC y RLC es esencial para comprender cómo la resistencia altera el patrón de oscilación de cualquier circuito eléctrico.

#### Objetivos 

-	Modelar las oscilaciones del circuito en función del valor de la resistencia, la inductancia y la capacitancia.
-	Examinar los tipos de amortiguación por medio de la visualización (gráficos y animaciones) del comportamiento del circuito para diferentes valores de la resistencia.
-	Implementar lo aprendido en clase sobre la Programación Orientada a Objetos (POO) de una manera coherente para una mejor organización y reutilización del código a futuro.

#### Descripción General del Código

1. Implementación de POO
Para modelar el problema del circuito RLC, se emplea la herencia múltiple, abstracción y polimorfismo.
  •	La clase base es un circuito LC (sin resistencia), y la clase derivada es el circuito RLC que añade la resistencia.
  •	Esto nos permite definir clases reutilizables y bien estructuradas.
  •	Se aplican los principios de abstracción para ocultar detalles internos y facilitar la interacción a través de métodos específicos.
2. Encapsulación
Los atributos clave del circuito, como la resistencia $R$, la inductancia $L$ y la capacitancia $C$, están encapsulados utilizando el decorador `@property` para garantizar un acceso controlado. Esto asegura que los parámetros del circuito puedan leerse o modificarse de forma segura sin interferir directamente con los atributos internos.
3. Decoradores Adicionales
Se ha añadido un decorador `@property` para permitir que algunos valores, como la frecuencia natural del circuito y el factor de amortiguamiento, se calculen sobre la marcha en lugar de almacenarse explícitamente. Esto es útil para extender la funcionalidad de la clase sin modificar el flujo principal del programa.
4. Método Numérico
  El método de integración de Euler se implementa para resolver la ecuación diferencial del circuito RLC. El método Euler es un método numérico iterativo simple que permite aproximar la solución en cada paso de tiempo utilizando un esquema de diferencias finitas.
  La ecuación diferencial que describe el circuito RLC es:

  $$L  \frac {d^2q(t)}{dt^2}+R \frac{dq(t)}{dt}+\frac{1}{C} q(t)=V_{in} (t)$$
  
  Donde $q(t)$ es la carga en el capacitor y $V_{in}(t)$ es el voltaje aplicado.
Esta ecuación se resuelve iterativamente para determinar la corriente y el voltaje en el circuito en función del tiempo.

5. Visualización y Animación
  Se ha utilizado *Matplotlib* para la creación de gráficos y animaciones.
  -	El gráfico muestra la oscilación de la corriente a través del circuito en función del tiempo.
  -	También se ha implementado una animación que ilustra cómo la corriente oscila (o se amortigua) dependiendo del valor de la resistencia.
  -	La animación permite visualizar el comportamiento subamortiguado, críticamente amortiguado y sobreamortiguado.

6. Modularización y Generalización
  El código está altamente modularizado. Esto significa que las diferentes partes del código, como las clases para el circuito y las funciones numéricas, están separadas y organizadas en módulos que pueden ser reutilizados en futuros proyectos.
  -	Por ejemplo, se puede implementar fácilmente un circuito diferente agregando una nueva clase sin modificar gran parte del código existente.
  El código está escrito siguiendo las buenas prácticas de programación aprendidas en clase, asegurando que sea limpio, comentado y fácil de seguir. Se han agregado comentarios detallados en cada línea crítica del código para facilitar su comprensión por parte de otros programadores o estudiantes.
### Explicación del Código
1. **Clases del Circuito**
  - Clase Base: `CircuitoLC`
    Esta clase define el comportamiento básico de un circuito LC, es decir, un circuito que tiene solo una inductancia $L$ y una capacitancia $C$. La ecuación diferencial es:

 $$L  \frac {d^2q(t)}{dt^2}+ \frac{1}{C} q(t)=0$$
 
  El comportamiento de este circuito es el de una oscilación libre, sin amortiguamiento.
  - Clase Derivada: `CircuitoRLC`
    La clase derivada `CircuitoRLC` incluye la resistencia $R$, por lo que la ecuación diferencial es:

  $$L  \frac {d^2q(t)}{dt^2}+R \frac{dq(t)}{dt}+\frac{1}{C} q(t)=V_{in} (t)$$
  
  Este circuito tiene un comportamiento oscilatorio que depende del valor de la resistencia RRR. Si $R$ es pequeño, el circuito está subamortiguado y oscila. Si $R$ es grande, está sobreamortiguado y no oscila. En el caso crítico, $R$ es justo lo suficiente para evitar las oscilaciones.

2. **Resolución Numérica con el Método de Euler**
   
    Para resolver la ecuación diferencial, se utiliza el método de Euler, un método numérico iterativo que aproxima el valor de las       variables en pequeños pasos de tiempo ($\Delta t$). La evolución de la corriente $i(t)$ y la carga $q(t)$ se calcula en cada paso de tiempo.

3. **Animación con *Matplotlib***
   
    La biblioteca *Matplotlib* se usa para generar una animación que muestra cómo la corriente varía con el tiempo.
  -	La animación representa el comportamiento oscilatorio del circuito para diferentes valores de resistencia.
  -	También se incluye una gráfica que compara los tres regímenes: subamortiguado, críticamente amortiguado y sobreamortiguado.
  
4. **Ajuste de Parámetros**:

    El usuario puede ajustar parámetros como:
  - Resistencia $R$: Afecta el tipo de amortiguamiento.
  - Inductancia $L$ y Capacitancia $C$: Definen la frecuencia natural del sistema.
  - Voltaje $V_in$ : Puede ser ajustado para estudiar diferentes respuestas de entrada.

