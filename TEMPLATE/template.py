from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.chains import LLMChain

# Si estoy en el main saludo y cargo las variables de ambiente
if __name__ == "__main__":
    print("Buenos dias LangChain!")
    load_dotenv()


information = """
Elon Reeve Musk (Pretoria, 28 de junio de 1971), conocido como Elon Musk, es un empresario, inversor y magnate sudafricano que también posee las nacionalidades canadiense y estadounidense. Es el fundador, consejero delegado e ingeniero jefe de SpaceX; inversor ángel, director general y arquitecto de productos de Tesla, Inc.; fundador de The Boring Company; cofundador de Neuralink y OpenAI, aunque ya no tiene más participación en esta última por desacuerdos en el rumbo de la empresa, además de ser el director de tecnología de X Corp..5​ Con un patrimonio neto estimado en unos 207 mil millones de dólares en junio de 2023,6​ Musk es la persona más rica del mundo según el índice de multimillonarios de Bloomberg y la lista de multimillonarios en tiempo real de Forbes.7​8​

Musk nació de madre canadiense y padre sudafricano blanco, y se crio en Pretoria (Sudáfrica). Estudió brevemente en la Universidad de Pretoria antes de trasladarse a Canadá a los 17 años. Se matriculó en la Universidad de Queen y se trasladó a la Universidad de Pensilvania dos años después, donde se graduó en Economía y Física. En 1995 se trasladó a California para asistir a la Universidad Stanford, pero en su lugar decidió seguir una carrera empresarial, cofundando la empresa de software web Zip2 con su hermano Kimbal. La empresa fue adquirida por Compaq por 307 millones de dólares en 1999. Ese mismo año, Musk cofundó el banco online X.com, que se fusionó con Confinity en 2000 para formar PayPal. La empresa fue comprada por eBay en 2002 por 1500 millones de dólares.

En 2002, Musk fundó SpaceX, fabricante aeroespacial y empresa de servicios de transporte espacial, de la que es CEO e ingeniero jefe. En 2003, se unió al fabricante de vehículos eléctricos Tesla Motors, Inc. (ahora Tesla, Inc.) como presidente y arquitecto de productos, convirtiéndose en su consejero delegado en 2008. En 2006, ayudó a crear SolarCity, una empresa de servicios de energía solar que posteriormente fue adquirida por Tesla y se convirtió en Tesla Energy. En 2015, cofundó OpenAI, una empresa de investigación sin ánimo de lucro que promueve la inteligencia artificial amigable. En 2016, cofundó Neuralink, una empresa de neurotecnología centrada en el desarrollo de interfaces cerebro-ordenador, y fundó The Boring Company, una empresa de construcción de túneles. También acordó la compra de la importante red social estadounidense Twitter en 2022 por 44 000 millones de dólares. Musk también ha propuesto el hyperloop. En noviembre de 2021, el director general de Tesla fue la primera persona de la historia en acumular una fortuna de 300 000 millones de dólares.9​

Ha sido criticado por hacer declaraciones poco científicas y controvertidas. En 2018, fue demandado por la Comisión de Bolsa y Valores de Estados Unidos (SEC) por tuitear falsamente que había conseguido financiación para una adquisición privada de Tesla. Llegó a un acuerdo con la SEC pero no admitió su culpabilidad, renunciando temporalmente a su presidencia y aceptando limitaciones en su uso de Twitter. En 2019, ganó un juicio por difamación presentado contra él por un espeleólogo británico que asesoró en el rescate de la cueva de Tham Luang. Musk también ha sido criticado por difundir información errónea sobre la pandemia de COVID-19 y por sus otras opiniones sobre asuntos como la inteligencia artificial, las criptomonedas y el transporte público.

Infancia, juventud y formación
Sus padres, Errol Musk y Maye Haldeman,10​ se conocieron en la escuela secundaria. Él era un ingeniero y promotor inmobiliario sudafricano que en su día fue copropietario de una mina de esmeraldas en la República de Zambia, cerca del lago Tanganica11​12​13​14​ y concejal de Pretoria que se opuso a las políticas del apartheid y al Partido Nacional en Sudáfrica.15​16​ Su madre es nutricionista y modelo; oriunda de Canadá, se mudó a Pretoria en 1950.17​18​ Se casaron en 1970 y en tres años tuvieron tres hijos: Elon (28 de junio de 1971), Kimbal (20 de septiembre de 1972) y Tosca Musk (20 de julio de 1974).18​ La familia era muy rica en la juventud de Elon; su padre dijo una vez: "Teníamos tanto dinero que a veces ni siquiera podíamos cerrar nuestra caja fuerte".12​

Elon Musk creció en una casa grande con sus hermanos y varios primos. Su madre trabajó en casa como asesora nutricionista. En los fines de semana también trabajaba como modelo, por lo que sus hijos apenas veían a sus padres y tenían mucha libertad para perseguir sus intereses.
‘I was raised by books. Books, and then my parents.‘
‘Fui educado por libros. Libros, y después mis padres.’
Elon Musk
A los nueve años comenzó a programar un Commodore VIC-20 que tenía 8 kilobytes de memoria RAM.19​ A los diez años aprendió a programar.20​ A los doce años diseñó su primer programa, un videojuego del espacio llamado Blastar, y se lo vendió por el equivalente a 500 USD a la revista sudafricana PC and Office Technology. En 1984 publicaron las 167 líneas de código fuente y reseñaron «En este juego tienes que destruir un carguero extraterrestre que lleva bombas mortales de hidrógeno y Status Beam Machines. El programa hace un buen uso de los sprites y las animaciones, y en este sentido su lectura merece la pena».20​21​22​

El dinero que ganaba programando lo gastaba en cómics, ordenadores y juegos de rol como Dungeons & Dragons.23​

En 1979, para escapar de los maltratos de su marido, que solía golpearla, su madre Maye se divorció y se mudó a Durban. Errol reclamó en los tribunales los términos del divorcio.24​ En 1981 Elon decidió ir a vivir a Johannesburgo con su padre. Kimbal se unió a ellos cuatro años después.18​

En la escuela no tenía amigos y era maltratado por sus compañeros. Tras tomar clases de karate, judo, lucha y a los dieciséis años crecer hasta los 180 cm empezó a defenderse.25​ Consciente de que sería más fácil emigrar a Estados Unidos desde Canadá,26​ solicitó un pasaporte canadiense a través de su madre,27​28​ nacida en Regina, Saskatchewan, de padres estadounidenses. Mientras esperaba la documentación, asistió a la Universidad de Pretoria durante cinco meses; esto le permitió evitar el servicio militar obligatorio en Sudáfrica.28​

Como muchos de sus parientes vivían en el Oeste canadiense, en 1989 Elon, Kimbal y Tosca Musk, junto a Maye Haldeman, se mudaron a Kingston, Ontario.10​29​ Cuando llegó, todos los ahorros de Maye estaban bloqueados, por lo que tuvo que trabajar en varios empleos.[cita requerida] Alquiló un pequeño apartamento en Toronto donde estuvieron tres semanas retirando grapas del suelo y papel pintado de las paredes. En el proceso, Maye se cortó una mano y puso en riesgo sus trabajos como modelo. Con el primer dinero que ganó, Maye compró una alfombra gruesa para que pudieran dormir en el suelo del apartamento, y un ordenador para Elon.30​ Luego trabajó como investigadora en la Universidad de Toronto y, simultáneamente, impartía clases de nutrición y modelaje dos noches por semana y además trabajaba como asesora nutricionista y estudiaba para su segundo máster dietético. Sus tres hijos tuvieron que conseguir becas, pedir préstamos y trabajar para estudiar en la universidad. Muchas veces no podían comer carne roja ni una vez a la semana.30​

En 1992 Elon obtuvo una beca para estudiar Economía y Física en la Universidad de Pensilvania. Recibió sus títulos de economía y física del Wharton School en la Universidad de Pensilvania. Después se matriculó en Stanford para hacer el doctorado, pero a los dos días lo abandonó para iniciar su propia empresa.22​ En 1995 tuvo la intención de trabajar para Netscape y fue a sus oficinas, pero no se atrevió a hablar con nadie por timidez.19​

Uno de sus profesores en la Universidad de Pensilvania era director ejecutivo de una empresa en Los Gatos, Silicon Valley, dedicada a investigar ultracondensadores electrolíticos destinados a vehículos eléctricos. Elon trabajó un verano en la empresa Pinnacle Research. Esos ultracondensadores tenían una densidad energética muy alta, pero sus componentes químicos eran carísimos y se vendían por miligramos porque había muy pocas minas que los extrajeran y no eran escalables para su producción en masa.23​31​

Tras obtener sus licenciaturas, e inspirado por innovadores como Nikola Tesla,32​ decidió entrar en tres áreas en las que consideraba había «problemas importantes», como luego indicaría él mismo: «Una de ellas era internet, otra la energía renovable y la otra era el espacio».20
"""

summary_template = """
    given the information {information} about  a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

llm = OllamaLLM(temperature=0, model_name="llama3.1")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

print(chain.run(information=information))
