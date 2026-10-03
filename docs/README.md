# Informações dos Desenvolvedores

```text
Nome: Renato Lima do Nascimento        - rm570266
Nome: Renato Levy do Valle             - rm572352
Nome: Alexandre Martins Niewelt        - rm570614
```

# Introdução

O crescimento dos veículos elétricos está mudando a forma como condomínios residenciais, edifícios corporativos e campus universitários precisam lidar com o consumo de energia. Segundo dados da ABVE, o mercado brasieliro de veículos eletrificados vem crescendo em ritmo acelarado, com aumento expressivo nos emplacamentos em 2026. Esse avanço torna a infraestrutura de recarga um tema cada vez mais importante para locais onde várias pessoas compartilham o mesmo espaço físico e a mesma infraestrutura elétrica.

Em uma residência individual, a recarga de um veículo elétrico costuma ser mais simples de controlar, pois o consumo normalmente aparece na conta de energia do próprio morador. Porém, em uma infraestrutura compartilhada, como um condomínio, uma empresa ou uma universidade, o carregador pode ser usado por várias pessoas diferentes. Nesse caso, surgem desafios de gestão: identificar quem utilizou o carregador, medir quanto cada usuário consumiu, calcular oc usto individual, evitar cobranças injustas e oferecer transparência para usuários e administradores.

A Agência Nacional de Energia Elétrica (ANEEL) informa que a atividade de recarga de veículos elétricos pode ser realizada inclusive para fins de exploração comercial, com preços livremente negociados. Isso reforça a necessidade de sistemas capazes de registrar, organizar e demonstrar os dados de uso da infraestrutura. Sem esse controle, a recarga compartilhada pode gerar conflitos sobre pagamento, uso indevido, divisão de custos, ocupação do carregador e responsabilidade pela operação.

Outro ponto importante é que cada sessão de recarga gera dados úteis. Entre esses dados estão o horário de início, horário de término, duração da sessão, energia entregue em kWh, potência utilizada, identificação do usuário, identificação do veículo, status da recarga e possíveis falhas ou interrupções. Esses dados não servem apenas para cobrança: eles também podem indicar padrões de uso, horários de maior demanda, períodos de ociosidade, usuários recorrentes, anomalias de consumo e necessidades futuras de expansão da infraestrutura.

A International Energy Agency (IEA) destaca que a infraestrutura de recarga é um elemento essencial para apoiar adoção em massa dos veículos elétricos. Embora a recarga doméstica ainda seja muito relevante, locais compartilhados também ganham importância porque nem todos os usuários têm acesso a um carregador individual. Isso torna necessário pensar em soluções digitais que ajudem gestores a administrar o uso dos carregadores de forma organizada, transparente e escalável.

Então, como podemos transformar sessões de recarga em uma infraestrutura compartilhada em dados estruturados, rateio justo e inteligência acionável? 

O EV ChargeOps surge como uma proposta para resolver esse problema. A plataforma tem como objetivo organizar os dados das sessões de recarga, associar cada sessão a um usuário ou unidade, calcular o consumo individual, aplicar um modelo de rateio transparente e gerar informações úteis para gestores e usuários. Assim, o carregador deixa de ser apenas um equipamento físico de recarga e passa a fazer parte de um sistema de gestão orientado por dados. Portanto, o problema principal que o EV ChargeOps busca resolver é a falta de integração entre o uso físico do carregador, o ocntrole individual das sessões, o cálculo justo do consumo e a geração de informações para tomada de decisão. A solução proposta pretende transformar registros técnicos de recarga em uma base organizada de operação, cobrança e análsie de planejamento.

# EV ChargeOps - Frente 1: Contexto e Problema

---

## O que são infraestruturas de recarga compartilhada

Infraestrutura de recarga compartilahda são ambientes em que um ou mais carregadores de veículos elétricos são utilziados por diferentes usuários dentro de um mesmo espaço físico. Esse cenário pode existir em condomínios residenciais, edifícios corporativos, estacionamentos comerciais, universidades, hospitais, shoppings e centros empresariais.

Diferente de uma recarga residencial individual, em que o carregador normalmente está vinculado diretamente à conta de energia do prorietário do veículo, a recarga compartilhada exige controle coletivo. O mesmo equipamento pode ser usado por moradores, funcionários, visitantes, alunos ou prestadores de serviço. Por isso, a gestão precisa responder a perguntas como: quem utilizou o carregador, por quanto tempo, quanta energia foi consumida, qual valor deve ser cobrado e como evitar conflitos entre usuários.

Segundo a International Energy Agency (IEA), a expansão da infraestrutura de recarga é um dos fatores necessários para sustentar o crescimento dos veículos elétricos. Em locais compartilhados, essa infraestrutura precisa ser acompanhada de sistemas de gestão capazes de organizar o uso, controlar acesso e transformar dados de recarga em informação operacional.

Nos condomínios, o desafio principal está no rateio justo do consumo. Em empresas e campus universitários, o problema envolve também controle de acesso, uso por perfis diferentes, relatórios gerenciais e planejamento da expansão da infraestrutura. Em todos os casos, o carregador deixa de ser apenas um equipamento elétrico e passa a fazer parte de um sistema de operação compartilhada.

## Principais desafios operacionais 

Os principais desafios enfrentados por gestores de condomínios, edifícios corporativos e campus universitários são: 

1. Identificação do usuário: é necessário saber quem iniciou a sessão de recarga. Essa identificação pode ocorrer por aplicativo, cartão RFID, login, QR Code ou outro mecanismo de autenticação
2. Medição individual do consumo: a gestão precisa medir quantos kWh foram entrgues em cada sessão para evitar cobrança genérica ou injusta.
3. Definição de modelo de cobrança ou rateio: o administrador precisa decidir se a recarga será gratuita, cobrada por kWh, por tempo, por assinatura ou dividida entre usuários.
4. Transparência para o usuário: o usuário precisa visualizar quanto carregou, quanto consumiu e quanto deverá pagar.
5. Controle de disponibilidade: em locais com poucos carregadores, é necessário acompanhar horários de pico, tempo de ocupação e possíveis períodos de ociosidade.
6. Tratamento de exceções: sessões interrompidas, falhas de comunicação, erro de identificação, usuário que não carregou no mês e múltiplos veículos da mesma unidade precisam ser tratados por regras claras.
7. Relatórios para tomada de decisão: o gestor precisa de dados para avaliar demanda, justificar expansão da infraestrutura, identificar gargalos e acompnhar custos.

A Alternative Fuels Data Center (AFDC), vinculada ao Departamento de Energia dos Estados Unidos, destaca que capturar e analisar dados de disponibilidade e utilização é uma parte importante da gestão de estações de recarga. Esses dados podem ser obtidos por portais de redes de carregamento, medidores separados, softwares de análise ou soluções fornecidas pelo fabricante do equipamento.

## Como funciona uma sessão de recarga 

Uma sessão de recarga é o período entre o início e o encerramento do carregamento de veículo elétrico. Do ponto de vista técnico e operacional, ela pode ser dividida em etapas.

Primero, o usuário se identifica na plataforma ou no carregador. Essa identificação pode ocorrer por cartão RFID, aplicativo, Bluetooth, login QR Code ou outro método disponível. Depois, o veículo é conectado ao carregador por meio de cabo de recarga. O carregador verifica se há comunicação com o veículo, se a conexão está correta e se o usuário está autorizado a iniciar a operação.

Após a autorização, a sessão é iniciada. O carregador começa a fornecer energia ao veículo e registra informações como horário de início, potência instantânea, energia acumulada, status da sessão e possíveis eventos. Durante a recarga, esses dados podem ser enviados para uma plataforma de gestão por rede cabeada, Wi-Fi, API ou protocolo de comunicação.

Em sistemas compatíveis com protocolos abertos, como OCPP (Open Charge Point Protocol), o carregador pode enviar eventos de início e fim de sessão, valores de medição, notificações de status e informações de transações, fim de transações, valores medidos e notificações de status.

Quando a recarga termina, a sessão é encerrada. Isso pode acontecer porque a bateria atingiu o nível desejado, porque o usuário interrompeu a sessão, porque o veículo foi desconectado ou porque ocorreu alguma falha. Ao final, o sistema registra os dados consolidados da sessão: energia total entregue, duração, horário de encerramento, usuário, veículo, carregador utilizado e status final

## Quais dados são gerados em uma sessão de recarga 

Cada sessão de recarga gera dados que podem ser usados para cobrança, rateio, auditoria e inteligência operacional.

Os principais dados são: 

* identificação da sessão;
* identificação do usuário;
* identificação da unidade, apartamento, setor ou matrícula;
* identificação do veículo, quando disponível;
* identificação do carregador;
* data e horário de início;
* data e horário de encerramento;
* duração total da sessão;
* energia entregue em kWh;
* potência média;
* potência máxima;
* status da sessão;
* forma de autenticação utilizada;
* eventos de erro ou interrupção;
* tempo de ocupação da vaga;
* valor estimado da recarga;
* regra de cobrança aplicada.

Esses dados têm valor operacional porque permitem entender não apenas quanto foi consumido, mas também como a infraestrutura está sendo usada. Por exemplo, o gestor pode descobrir quais horários têm maior demanda, quais usuários utilizam mais o carregador, se há sessões muito longas com pouca energia entregue, se existem falhas recorrentes ou se a infraestrutura atual está próxima do limite de uso.

ALém disso, dados como energia entregue, tempo de sessão e identificação do usuário são essenciais para calcular uma fatura individual. Sem esses registros, o custo da recarga tender a ser dividido de forma genérica, o que pode prejudicar quem usa pouco e beneficiar quem usa muito.

## Modelos de negócio para recarga compartilhada

Existem diferentes formas de organizar financeiramente a recarga compartilhada. A escolha do modelo depende do tipo de ambiente, do objetivo da gestão e das regras interna do local.


| Modelo             | Como funciona                                                                                                 | Vantagens                                                             | Limitações                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Recarga gratuita   | O usuário não paga diretamente pela recarga. O custo é assumido pelo condomínio, empresa, campus ou operador. | Simples para o usuário e pode incentivar o uso de veículos elétricos. | Pode gerar uso excessivo, falta de controle e transferência injusta de custo para quem não utiliza. |
| Cobrança por kWh   | O usuário paga de acordo com a energia efetivamente consumida.                                                | É o modelo mais próximo do consumo real e favorece rateio justo.      | Exige medição confiável e integração com dados da sessão.                                           |
| Cobrança por tempo | O usuário paga pelo tempo de uso ou ocupação do carregador.                                                   | Ajuda a reduzir ocupação excessiva e incentiva rotatividade.          | Pode ser injusto quando veículos carregam em velocidades diferentes.                                |
| Assinatura mensal  | O usuário paga um valor fixo mensal para ter acesso à infraestrutura.                                         | Facilita previsibilidade de receita e simplifica cobrança.            | Pode ser injusto se usuários consumirem quantidades muito diferentes de energia.                    |
| Rateio condominial | O custo é dividido entre unidades ou usuários conforme uma regra definida pelo condomínio.                    | Pode ser adaptado às regras internas do local.                        | Precisa de critérios claros para evitar conflitos.                                                  |
| Modelo híbrido     | Combina consumo por kWh com taxa fixa, taxa de manutenção ou cobrança por ociosidade.                         | Permite cobrir energia, operação, manutenção e uso da vaga.           | Exige regras bem documentadas e transparência para o usuário.  

No Brasil, a ANEEL informa que é permitida a realização de atividades de recarga de veículos elétricos, inclusive com exploração comercial e preços livremente negociados. Isso permite que diferentes modelos sejam avaliados, desde que a operação respeite as regras aplicáveis, a comunicação com a distribuidora quando exigida e a transparência para os usuários.

Em mercados internacioanis, também existem modelos variados. Redes de recarga podem cobrar por kWh, por tempo, por sessão, por planos mensais ou combinar tarifas diferentes conforme localização, potência, horário e perfil do usuário. A página de preços da EVgo, por exempllo, mostra planos com mensalidade, descontos por plano e cobrança por sessão em determinados casos. Já análises de mercado como a da eMabler, apontam que modelos por kWh, por tempo e tarifas dinâmicas são usados em diferentes contextos operacionais.

## Opção A - Análise de Mercado

A análsie de mercado tem como objetivo comparar o EV ChargeOps com soluções já existentes no setor de recarga de veículos elétricos. Essa etapa ajuda a equipe a entender quais problemas o mercado já resolve, quais funcionalidades são comuns, quais modelos de negócio são utilizados e quais lacunas ainda podem ser exploradas.

### Zaptec 

**Nome da solução:** Zaptec Pro e Zaptec Portal.

**Problema que resolve:**
A Zaptec atua no problema de recarga compartilhada em locais com múltiplos usuários e múltiplos carregadores, como condomínios, edifícios residencaiis, empresas e estacionamentos. A solução busca permitir que vários veículos carreguem ao mesmo tempo sem sobrecarregar a instalão elétrica.

Segundo a página do Zaptec Pro, o sistema utiliza balanceamento dinâmico de carga e de fases para distribuir melhor a energia disponível entre os veículos. Já o Zaptec Portal permite acompanhar o uso em tempo real, visualizar histórico de carregamento e controlar o acesso de usuários.

**Funcionalidades Principais:**

* carregadores inteligentes para uso comercial e compartilhado;
* balanceamento dinâmico de carga;
* balanceamento entre fases;
* monitoramento em tempo real;
* histórico de carregamento por instalação, carregador ou usuário;
* controle de acesso por usuário;
* possibilidade de restringir ou liberar o uso dos carregadores;
* plataforma em nuvem para gestão da infraestrutura.

**Modelo de negócio:**
O modelo da Zaptec combina venda de hardware, como carregadores e dispositivos de balanceamento, com uso de plataforma digital de gestão. A empresa atua principalmente como fabricante e fornecedora de soluções para instalações residenciais, comerciais e compartilahdas. 

**Limitações conhecidas:** 
A Zaptec é uma solução robusta para infraestrutura de recarga, mas seu foco principal está no ecossistema próprio de carregadores, portal e dispositivos. Para um projeto como o EV ChargeOps, isso mostra uma possível limitação: a solução depende da adoção do ambiente Zaptec e não necessariamente resolve, de forma personalizada, regras locais de rateio condominial, integração com sistemas internos brasileiros ou uso de IA para análise operacional específica. 

Além disso, uma solução desse tipo pode ser mais adequada para instalações planejadas desde o início com o ecossistema da marca. Em cenários onde o carregador já é de outro fabricante, como no caso do GoodWe HCA G2 do desafio, seria necessário avaliar a compatiblidade técnica e os protocolos disponíveis.

### Wallbox Pulsar Plus 

**Nome da solução:** Wallbox Pulsar Plus

**Problema que resolve:** 
O Wallbox Pulsar Plus resolve o problema da recarga inteligente em ambientes residenciais e multifamiliares. Ele é um carregador compacto, conectado e voltado para usuários que precisam de uma solução de recarga mais controlada do que uma tomada comum.

A página oficial do Wallbox Pulsar Plus informa que o equipamento possui conectividade Bluetooth e Wi-Fi, identificação de usuário via aplicativo, monitoramento de uso de energia, agendamento de sessões e recursos de gerenciamento de energia quando combinado com acessórios como Wallbox Power Meter.

**Funcionalidades Principais:** 
* carregamento AC;
* potência de até 11,5 kW, dependendo da versão e da instalação;
* conectividade via Bluetooth e Wi-Fi;
* controle pelo aplicativo Wallbox;
* agendamento de sessões de recarga;
* monitoramento do uso de energia;
* identificação de usuário pelo aplicativo;
* recursos de gerenciamento de energia;
* gerenciamento dinâmico de carga com acessórios de medição;
* possibilidade de integração com energia solar em determinados cenários.

**Modelo de negócio:**
O modelo de negócio do Wallbox Pulsar Plus é baseado principalmente na venda do carregador, acessórios e uso do aplicativo da marca. A empresa também possui soluções para negócios e carregamento público, mas o Pulsar Plus é apresentado principalmente como uma solução de carregamento residencial e multifamiliar.

**Limitações conhecidas:** 
Embora o pulsar seja um carregador inteligente, ele não é, sozinho, uma solução completa de rateio condominial. Ele permite controlar e monitorar a recarga, mas a plataforma do EV ChargeOps precisaria ir além: organizar sessões por usuário, calcular valores individuais, tratar exceções e gerar faturas mensais.

Outra limitação observada é que alguns recursos dependendem de acessórios ou condições específicas. Por exemplo, o gerenciamento de carga depende de um medidor de energia adicional, e a própria págian da Wallbox informa que o recuros de carregamento solar não é compatível com instalações com múltiplos carregadores e OCPP.

### ChargePoint

**Nome da solução:** ChargePoint Plataform

**Problema que resolve:** 
A ChargePoint atua em uma escala mais ampla, oferecendo uma plataforma para operação de redes de recarga em empresas, frotas, estacionamentos, locais públicos, edifícios comerciais e ambientes corporativos. O problema central que ela resolve é a gestão completa de estações de recarga, incluindo controle de acesso, precificação, monitoramento, relatórios e integração com outros sistemas.

 A página oficial de software da ChargePoint apresenta recursos como gerenciamento de estações, assistência por IA, integrações por API, políticas de acesso , preços dinâmicos e relatórios operacionais. A empresa também destaca soluções para locais de trabalho, com controle de preço, acessibilidade, uso de energia, lista de espera e monitoramento em tempo real.

**Funcionalidades Principais:** 
* gerenciamento de estações de recarga;
* controle remoto de acesso;
* definição de políticas de uso;
* preços dinâmicos por tipo de usuário, duração, custo de energia e horário;
* monitoramento de saúde das estações;
* relatórios e analytics;
* suporte a usuários;
* aplicativo para motoristas;
* roaming e integração com parceiros;
* APIs abertas e integrações com outros sistemas;
* recursos de assitência por IA para operação.

**Modelo de negócio:**
O modelo de negócio da ChargePoint combina hardware, software, serviços de rede, suporte e soluções para empresas. Uma limitação que pode ser citada é que a plataforma global pode não atender diretamente às regras específicas de rateio condominial brasileiro, às necessidades de integração com um carregador GoodWe HCA G2 ou às particularidades de uma gestão local feita por condomínio, empresa ou campus.

**Limitações conhecidas:** 
O ChargePoint é uma solução muito completa, mas também mais ampla e corporativa. Para o contexto do EV ChargeOps, isso pode significar complexidade maior do que a necessária para um protótipo 

### NeoCharge

**Nome da solução:** NeoCharge

**Problema que resolve:** 
A NeoCharge atua no mercado brasileiro de carregadores, instalação e soluções para recarga de veículos elétricos. No contexto de prédios e condomínios, a empresa ajuda a resolver o problema da instação, da escolha do carregador, da adaptação elétrica e da gestáo do uso coletivo. 

No guia da NeoCharge sobre carregador para carro elétrico em prédios e condomínios, instalações e soluções para recarga de veículos elétricos. No contexto de prédios e condomínios, a empresa ajuda a resolver o problema da instalação, da escolha do carregador, da adaptação elétrica e da gestão do uso coletivo.

No guia da NeoCharge sobre carregador para carro elétrico em prédios e condomínios, a empresa destaca pontos importantes para esse tipo de ambiente, como aprovação em assembleia, definição de quem usará o carregador, localização do equipamento, rateio dos custos de instalação, cobrança pelo uso e contratação de empresa especializada.

A Página também explica que, em uso coletivo, carregadores inteligentes podem ser associados a plataformas de gerenciamento para medir quantos kWh cada morador utilizou e permitir a divisão mensal dos custos.

**Funcionalidades Principais:** 
* venda de carregadores para veículos elétricos;
* orientação sobre instalação em residências, prédios e condomínios;
* suporte ao planejamento de infraestrutura;
* explicação sobre rateio e cobrança em condomínios;
* carregadores inteligentes com controle e monitoramento;
* aplicativo NeoCarge para localizar elepostos e gerenciar recargas;
* soluções de recarga para diferentes perfis de uso.

**Modelo de negócio:**
O modelo da NeoCharge envolve venda de equipamentos, suporte à instalação, comercialização de carregadores e oferta de soluções relacionadas à recarga. No Brasil, seu diferencial está em tratar diretamente questões práticas de instalação, infraestrutura e uso em condomínios.

**Limitações conhecidas:** 
A NeoCharge oferece uma abordagem muito próxima da realidade brasileira, mas seu conteúdo público enfatiza mais a instalação, a escolha de equipamentos e a gestão prática do carregador. Para o EV ChargeOps, ainda existe espaço para propor uma camada mais estruturada de dados, IA, cálculo de fatura, tratamento de exceções e inteligência operacional para gestores. 

Outra limitação é que as soluções de mercado podem depender de equipamentos específicos, aplicativos próprios ou plataformas parceiras. O EV ChargeOps precisa ser documentado como uma solução capaz de trabalhar a partir dos dados da sessão de recarga e do carregador utilizado no desafio.

### Comparação entre as soluções analisadas 


| Solução             | Foco principal                                          | Funcionalidades fortes                                                            | Limitação para o contexto do EV ChargeOps                                                               |
| ------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Zaptec              | Recarga compartilhada e balanceamento de carga          | Controle de acesso, histórico, balanceamento dinâmico, portal em nuvem            | Depende do ecossistema Zaptec e pode não se adaptar diretamente ao carregador GoodWe                    |
| Wallbox Pulsar Plus | Recarga residencial e multifamiliar inteligente         | App, Wi-Fi, Bluetooth, agendamento, monitoramento de energia                      | Não resolve sozinho o rateio condominial completo e pode depender de acessórios                         |
| ChargePoint         | Plataforma ampla de gestão de redes de recarga          | Preços dinâmicos, analytics, API, controle de acesso, suporte operacional         | Pode ser complexa e ampla demais para um cenário local específico                                       |
| NeoCharge           | Mercado brasileiro, instalação e recarga em condomínios | Orientação para prédios, venda de carregadores, gestão prática e controle por kWh | Enfatiza instalação e operação, mas não necessariamente uma camada própria de IA e fatura personalizada |

# EV ChargeOps - Frente 2: Base Regulatória e Técnica

---

# Mapeamento Regulatório Completo - Carregadores Compartilhados de Veículos Elétricos

Estado de São Paulo - Conformidade Jurídica e Técnica

Federal · Estadual · Municipal · ANEEL · Distribuidora · Bombeiros · Tributário

## Mapa Geral do Arcabouço Regulatório

| Nível | Norma/Ato | Objeto | Vigência |
|---|---|---|---|
| Federal (ANEEL) | RN ANEEL 1.000/2021 (arts. 550 a 560) | Regra-mãe: recarga de VE, protocolos abertos, comunicação prévia e exploração comercial. | 07/12/2021 |
| Federal (ANEEL) | RN ANEEL 819/2018 (revogada) | Primeira regulação federal de recarga; conteúdo incorporado pela RN 1.000/2021. | Revogada |
| Estadual SP | Lei Estadual 18.403/2026 | Direito do condômino de instalar recarga em vaga privativa e previsão de infraestrutura em novos empreendimentos. | 19/02/2026 |
| Estadual SP | Decreto Estadual 69.118/2024 | Regulamento de Segurança Contra Incêndio das edificações e áreas de risco. | 09/12/2024 |
| Estadual SP (Bombeiros) | Portaria CCB 003/970/2026 - IT-41 revisada | Normas técnicas para SAVE em edificações; referência a NBR 5410, NBR 17019 e NBR IEC 61851-1. | 17/03/2026 |
| Municipal SP | Lei Municipal 17.336/2020 | Edifícios novos da cidade de SP devem prever solução de recarga com medição individualizada. | 30/03/2020 |
| Municipal SP | Lei Municipal 18.229/2025 | Referência do documento original; fonte oficial localizada não confirma relação com recarga de VE. Conferir antes de uso jurídico. | 16/01/2025 |
| Distribuidora Enel SP | CNC-OMBR-MAT-19-0280-EDBR | Especificação técnica para conexão de estações de recarga de VE. | Vigente |
| Tributário (SEFAZ-SP) | RC 31007/2024 e RC 30579/2024 | Posição SEFAZ-SP: incidência de ICMS na comercialização de energia via eletroposto. | Publicadas em 2025 |
| Tributário (Municipal SP) | Posição municipal / ISS | Discussão sobre enquadramento como prestação de serviço; controvérsia ativa. | Controvérsia ativa |
| ABNT (NBR) | NBR 5410, NBR 17019, NBR IEC 61851-1 | Normas técnicas de instalações elétricas e sistemas de recarga condutiva para VE. | Vigentes |

## Nível Federal: RN ANEEL 1.000/2021

A RN ANEEL 1.000/2021 é a norma federal de referência para o serviço público de distribuição de energia elétrica. Seus arts. 550 a 560 regulam instalações de recarga de veículos elétricos e são diretamente aplicáveis a carregadores compartilhados em São Paulo.

| Artigo | Tema | Regra para carregador compartilhado |
|---|---|---|
| Art. 550 | Comunicação prévia | Obrigatória se houver conexão nova, alteração de carga ou alteração do nível de tensão. |
| Art. 552 | Protocolos abertos | Obrigatório para equipamentos compartilhados: comunicação, supervisão e controle remotos. Na prática, exige compatibilidade com protocolo aberto como OCPP. |
| Art. 553 | Normas técnicas | ANEEL prevalece; depois normas técnicas da ABNT; depois normas e padrões da distribuidora. |
| Art. 554 | Exploração comercial | Permitida, com preço livre e sem autorização especial da ANEEL. O operador não precisa de outorga específica. |
| Art. 555 | Vedação V2G | O veículo não pode injetar energia na rede. V2H na mesma unidade consumidora é permitido. |
| Art. 556 | Ressarcimento de danos | A distribuidora pode ser responsável por ressarcimento de danos elétricos ao veículo conectado, conforme as regras aplicáveis. |

Comentário: A RN 1.000/2021 criou um regime favorável ao mercado de recarga compartilhada: qualquer pessoa física ou jurídica pode operar comercialmente, com preço livre. A exigência técnica adicional mais relevante para carregadores compartilhados é o protocolo aberto previsto no art. 552.

## Nível Estadual: legislação e bombeiros de São Paulo

2.1 Lei Estadual nº 18.403/2026. Assegura ao condômino o direito de instalar, às suas expensas, estação de recarga individual para veículo elétrico em sua vaga de garagem privativa, desde que respeitadas normas técnicas e de segurança. Também exige previsão de capacidade mínima em novos empreendimentos, a ser regulamentada pelo Executivo.

| Requisito da Lei 18.403/2026 | Aplicação ao carregador compartilhado |
|---|---|
| Instalação em vaga privativa - direito individual | Carregador compartilhado em área comum não é direito individual automático; depende de deliberação coletiva em assembleia. |
| Compatibilidade com a carga elétrica da unidade | Avaliação técnica obrigatória, especialmente para carregadores de maior potência. |
| Conformidade com normas da distribuidora, ABNT e segurança | Aplicação conjunta de normas Enel, ABNT e Corpo de Bombeiros. |
| Instalação por profissional habilitado com ART/RRT | Obrigatória; instalação improvisada aumenta risco técnico, securitário e regulatório. |
| Comunicação formal prévia ao condomínio | Necessária para vagas privativas; área comum exige deliberação condominial. |
| Projetos novos: previsão de capacidade elétrica | Empreendimentos aprovados após a lei devem prever infraestrutura futura; critérios dependem de regulamentação. |

Atenção: A Lei 18.403/2026 trata principalmente de vaga privativa. Hubs de recarga em áreas comuns de condomínios devem ser aprovados coletivamente, conforme regras condominiais e parecer técnico.

### Bombeiros: portaria CCB 003/970/2026 - IT-41 revisada

2.2 Decreto Estadual nº 69.118/2024. Institui o Regulamento de Segurança Contra Incêndios das edificações e áreas de risco no Estado de São Paulo. Serve como base para exigências do Corpo de Bombeiros relacionadas a garagens e SAVE.

2.3 Portaria CCB nº 003/970/2026. Atualiza a IT-41 para incluir Sistemas de Alimentação de Veículos Elétricos (SAVE) em edificações, com exigências de projeto, proteção elétrica, sinalização e modos de recarga.

| Exigência da Portaria 003/970/2026 | Status / Observação |
|---|---|
| Projeto técnico por profissional habilitado com ART/RRT | Obrigatório. |
| Conformidade com NBR 5410 | Norma-base para instalações elétricas de baixa tensão. |
| Conformidade com NBR 17019 | Específica para alimentação de veículos elétricos em locais especiais. |
| Conformidade com NBR IEC 61851-1 | Define modos de recarga e requisitos gerais do sistema de recarga condutiva. |
| Apenas Modos 3 e 4 em áreas internas | Modos 1 e 2 são proibidos em ambientes fechados; wallbox e DC fast são permitidos quando conformes. |
| Circuito exclusivo por SAVE + disjuntor + DR + DPS | Sem tomadas comuns, extensões ou adaptadores. |
| Chave de emergência individual a menos de 5 m de cada SAVE | Desligamento manual rápido em emergência. |
| Ponto de desligamento por pavimento a menos de 5 m da entrada | Controle coletivo por andar. |
| Sinalização fotoluminescente padronizada | Identificação visual dos pontos de recarga. |
| Sprinklers, detectores e exaustão | Pontos ainda em discussão; acompanhar novas consultas e versões da IT. |

Comentário: A Portaria reduziu o vazio regulatório sobre segurança contra incêndio para SAVE em edificações e tornou a conformidade elétrica e documental um ponto central para AVCB e seguros.

## Nível Municipal: leis da cidade de São Paulo

3.1 Lei Municipal nº 17.336/2020. Obriga edifícios residenciais e comerciais novos da cidade de São Paulo a preverem solução para recarga de veículos elétricos, com modo de recarga conforme normas técnicas brasileiras e medição individualizada do consumo.

Comentário: O ponto crítico para carregadores compartilhados é a medição individualizada: a cobrança deve refletir o consumo de cada usuário, evitando rateio genérico em áreas comuns.

3.2 Lei Municipal nº 18.229/2025. O documento original cita esta lei como complementação de recarga. Contudo, a fonte oficial localizada apresenta ementa distinta, sem confirmação de vínculo com recarga de veículos elétricos. Recomenda-se validação jurídica antes de manter essa norma como referência material.

| Aspecto | Lei Municipal 17.336/2020 | Lei Municipal 18.229/2025 | Lei Estadual 18.403/2026 |
|---|---|---|---|
| Âmbito | Cidade de SP | Cidade de SP - referência a conferir | Estado de SP |
| Foco principal | Novos prédios: prever solução de recarga | Não confirmado em fonte oficial como norma de recarga | Vagas privativas e capacidade em novos empreendimentos |
| Medição individual | Exige expressamente | Não confirmado | Remete a normas técnicas e da distribuidora |
| Direito ao condômino | Não trata | Não confirmado | Garante direito individual para vaga privativa |
| Novos empreendimentos | Obrigatório, conforme regulamentação | Não confirmado | Obrigatório, com critérios a regulamentar |
| Custo da instalação | Conforme modelo condominial/empreendimento | Não confirmado | Condômino, para vaga privativa |

### Normas da Distribuidora: ENEL São Paulo

A especificação técnica CNC-OMBR-MAT-19-0280-EDBR define critérios para conexão de estações de recarga de veículos elétricos, incluindo solicitações de ligação nova, alteração de carga e cadastro das estações junto à ANEEL.

| Exigência Enel SP | Tipo de instalação | Detalhe |
|---|---|---|
| Comunicação prévia obrigatória | Conexão nova, alteração de carga ou nível de tensão | Preencher formulário/cadastro específico para EVSE. |
| Ponto de medição: privativo | Local privado, uso exclusivo do titular da UC | Em geral, não há medição adicional exclusiva para a EVSE. |
| Ponto de medição: semi-público | Condomínio, shopping, hotéis, eletroposto compartilhado | Pode ser conectado na UC da administração ou em UC adicional exclusiva. |
| Medição exclusiva para eletroposto | Carregador comercial/público | Possível em ponto de conexão exclusivo, mediante solicitação. |
| DPS obrigatório | Todos os tipos | Dispositivo de Proteção contra Surtos obrigatório. |
| Restrição V2G | Todos os tipos | Vedada injeção de energia na rede. |
| Cadastro na ANEEL | Distribuidora faz o cadastro | Informações são reportadas periodicamente à ANEEL. |

Comentário: Para carregadores compartilhados, a UC dedicada ajuda a separar a conta de energia do condomínio ou estabelecimento e facilita gestão, faturamento e rastreabilidade regulatória.

### Controvérsia Ttributária: ICMS x ISS em São Paulo

A tributação da recarga de veículos elétricos é um ponto de insegurança jurídica. A SEFAZ-SP possui respostas formais indicando incidência de ICMS sobre fornecimento de energia para recarga de veículos de terceiros; operadores também discutem enquadramentos de ISS conforme modelo de prestação de serviço.

| Tributo | Quem defende | Fundamento | Alíquota efetiva | Posição formal |
|---|---|---|---|---|
| ICMS (Estado SP) | SEFAZ-SP | CF/88 art. 155; energia elétrica como mercadoria; respostas à consulta. | 18% sobre valor cobrado, conforme entendimento estadual indicado no documento original. | RC 31007/2024 e RC 30579/2024. |
| ISS (Município SP) | Prefeitura / operadores | LC 116/2003; tese de prestação de serviço. | 2% a 5%, conforme lista e enquadramento municipal. | Controvérsia; sem ato formal consolidado no documento original. |

| Cenário | Impacto prático | Risco |
|---|---|---|
| Recolher ICMS | Carga tributária alta; possível crédito do ICMS pago na compra de energia, conforme caso. | Pode impactar margem e viabilidade do modelo. |
| Recolher ISS | Carga menor; prática relatada entre operadores. | Risco de autuação estadual, se prevalecer a tese de ICMS. |
| Não recolher nenhum | Pode ocorrer em fases iniciais, mas não é recomendável. | Risco elevado de autuação fiscal. |
| Aguardar reforma tributária | IBS/CBS substituem a lógica ICMS/ISS no longo prazo. | Insegurança permanece durante a transição. |

Atenção: Antes de iniciar operação comercial em São Paulo, recomenda-se consulta tributária especializada. O tratamento fiscal pode afetar preço, nota fiscal, cadastro e passivo tributário.

### Linha do Tempo Regulatória - São Paulo

| Data | Ato | Impacto |
|---|---|---|
| Jun/2018 | RN ANEEL 819/2018 | Primeira regulação federal de recarga de VE no Brasil. |
| Mar/2020 | Lei Municipal SP 17.336/2020 | Prédios novos em SP devem prever recarga e medição individual. |
| Dez/2021 | RN ANEEL 1.000/2021 | Consolidação das regras de distribuição; arts. 550 a 560 tratam de recarga de VE. |
| Set/2023 | Norma Enel SP 0280-EDBR | Especificação técnica de conexão para EVSE atualizada. |
| Dez/2024 | Decreto Estadual 69.118/2024 | Novo regulamento de segurança contra incêndio. |
| Jan/2025 | Lei Municipal SP 18.229/2025 | Referência original a conferir; fonte oficial localizada não trata de recarga de VE. |
| Nov/2025 | Portarias CCB-008/009 800/2025 | Consulta pública da IT-41 revisada. |
| Fev/2026 | Lei Estadual 18.403/2026 | Direito de instalação em vaga privativa. |
| Mar/2026 | Portaria CCB 003/970/2026 | Normas SAVE em garagens e exigências técnicas. |
| 2026-2027 | Novas consultas públicas previstas | Possíveis regras sobre sprinklers, exaustão e detectores. |
| 2033 | Reforma tributária - LC 214/2025 | IBS/CBS substituem progressivamente ICMS/ISS no novo sistema. |

Aviso: Este documento foi reformatado para leitura e não constitui assessoria jurídica, regulatória ou tributária. O cenário regulatório da eletromobilidade em São Paulo evolui rapidamente; acompanhe publicações oficiais da ANEEL, Corpo de Bombeiros SP, SEFAZ-SP, Prefeitura de São Paulo, Enel/Equatorial e ABNT.

## Normas ABNT aplicáveis

| Norma ABNT | Título | Relevância |
|---|---|---|
| NBR 5410:2004 e emendas | Instalações elétricas de baixa tensão | Norma-base de qualquer instalação elétrica; exigida em conjunto com Bombeiros e distribuidora. |
| NBR 17019:2022 | Instalações elétricas de baixa tensão - alimentação de VE | Específica para garagens, estacionamentos e locais com EVSE. |
| NBR IEC 61851-1:2021 | Sistema de recarga condutiva para VE - requisitos gerais | Define modos de recarga e requisitos gerais do EVSE. |
| NBR IEC 62196 | Plugues, tomadas e conectores para VE | Define tipos de conectores; relevante para hardware. |
| NBR 14136:2012 | Plugues e tomadas de uso doméstico e análogo | Aplicável a tomadas comuns; não recomendada para uso compartilhado em ambientes internos. |

Comentário: As três normas mais críticas para recarga compartilhada em São Paulo são NBR 5410, NBR 17019 e NBR IEC 61851-1. O OCPP não é norma ABNT, mas é o protocolo aberto usual para atendimento ao art. 552 da RN 1.000/2021.

# Visão geral das interfaces

| Interface | Tipo | Alcance típico | Destino / Integração | Papel principal na plataforma |
|---|---|---|---|---|
| RS-485 A1/B1 | Serial cabeada | Até 100 m | Inversor GoodWe (FV/bateria) via Modbus RTU | Smart charging solar, gestão de excedente FV, bateria e balanceamento dinâmico de carga. |
| RS-485 A2/B2 | Serial cabeada | Até 100 m | Medidor MID certificado via Modbus RTU | Medição certificada por sessão para reembolso, cobrança e auditoria. |
| LAN (RJ45) | Ethernet cabeada | Até 100 m por trecho | Roteador/switch -> Cloud SEMS | Canal preferencial para telemetria, monitoramento, API SEMS e firmware OTA. |
| Wi-Fi 2,4 GHz | Sem fio | 30-50 m em condição favorável | Roteador -> Cloud SEMS | Alternativa à LAN quando cabo não for viável; mesmos recursos cloud, menor robustez. |
| Bluetooth BLE | Sem fio curto alcance | Até 10 m | Smartphone do instalador via SolarGo | Onboarding, configuração local, Wi-Fi, RFID, parâmetros e diagnóstico presencial. |
| RFID 13,56 MHz | NFC local | < 5 cm | Cartão vinculado ao carregador | Autenticação física do usuário e início de sessão sem smartphone. |

Resumo de arquitetura: RS-485 resolve integração local e medição; LAN/Wi-Fi levam dados ao SEMS e à plataforma; Bluetooth serve ao instalador; RFID identifica usuários em campo.

## Modelos HCA G2 e premissas técnicas

A linha HCA G2 é composta por carregadores AC residenciais/comerciais leves com conector Tipo 2. A escolha do modelo impacta corrente, fases, infraestrutura elétrica e estratégia de balanceamento de carga.

| Modelo | Potência | Fases | Tensão de entrada | Corrente máxima | Conector |
|---|---:|---|---|---|---|
| GW7K-HCA-20 | 7 kW | Monofásico | 230 Vac, L/N/PE | 32 A | Tipo 2 (IEC 62196) |
| GW11K-HCA-20 | 11 kW | Trifásico | 400 Vac, 3L/N/PE | 16 A por fase | Tipo 2 (IEC 62196) |
| GW22K-HCA-20 | 22 kW | Trifásico | 400 Vac, 3L/N/PE | 32 A por fase | Tipo 2 (IEC 62196) |

### Mapa rápido: qual interface usar para cada objetivo?

| Objetivo da plataforma | Interface primária | Interfaces de apoio | Observação prática |
|---|---|---|---|
| Monitorar status, potência e energia de sessão | LAN ou Wi-Fi via SEMS/API | RS-485 MID para validação metrológica | LAN é preferível em condomínios e estacionamentos. |
| Controlar recarga conforme energia solar disponível | RS-485 A1/B1 com inversor | LAN/Wi-Fi para enviar dados ao cloud | A lógica pode rodar no próprio ecossistema GoodWe; integração externa depende de API/Modbus/OCPP. |
| Cobrar usuário por kWh ou gerar reembolso | RS-485 A2/B2 com medidor MID | RFID para identificar usuário | MID fornece base de medição; RFID vincula consumo à pessoa/perfil. |
| Cadastrar ou trocar rede Wi-Fi | Bluetooth BLE via SolarGo | - | Bluetooth é canal de configuração local, não de operação contínua. |
| Autenticar motorista sem aplicativo | RFID | LAN/Wi-Fi para sincronizar sessão | Bom para frotas, condomínios e usuários sem smartphone. |
| Integrar com backend próprio ou roaming | OCPP, se suportado/ativado | LAN + RFID | Ponto crítico: confirmar versão e ativação do OCPP com a GoodWe Brasil. |

## RS-485 (Modbus RTU): integração local com inversor e medição

O RS-485 é a interface local mais importante quando a plataforma precisa de smart charging solar, balanceamento de carga ou medição certificada. O HCA G2 possui dois pares independentes: A1/B1 para inversor GoodWe e A2/B2 para medidor MID.

| Parâmetro | Valor / detalhe | Uso pela plataforma |
|---|---|---|
| Tipo físico | Par trançado externo; cabeamento providenciado pelo instalador | Infraestrutura local entre carregador, inversor e/ou medidor. |
| Alcance máximo | Até 100 m no diagrama de arquitetura | Permite separar carregador do inversor ou quadro de medição dentro de garagem/edificação. |
| RS485_A1/B1 | Comunicação com inversor GoodWe FV/bateria | Leitura indireta de excedente FV, bateria e consumo da unidade para otimizar recarga. |
| RS485_A2/B2 | Comunicação com medidor MID certificado | Base para faturamento individualizado, reembolso corporativo e auditoria. |
| Protocolo | Modbus RTU | Integração técnica local possível, mas mapa completo de registradores deve ser solicitado à GoodWe. |
| Limitação | Canal local, cabeado, sem conexão direta à internet | Precisa de LAN/Wi-Fi/OCPP/API SEMS para integração cloud e backend externo. |

| Função habilitada pelo RS-485 | Como funciona | Como a plataforma pode usar |
|---|---|---|
| Smart charging solar | O carregador lê excedente FV via inversor e ajusta a potência de carga. | Aplicar regras de prioridade solar, reduzir custo da recarga e melhorar uso de geração local. |
| PV + Battery | Coordena recarga com inversor e bateria para aproveitar energia armazenada antes da rede. | Criar perfis de operação por usuário, horário, SoC e disponibilidade de energia. |
| Balanceamento dinâmico de carga | Recebe dados de consumo da unidade e reduz/pausa carga para evitar disparo do disjuntor. | Evitar sobrecarga em condomínios, residências e frotas com limite contratado. |
| Potência mínima garantida | Quando FV é insuficiente, complementa com rede ou bateria para manter potência mínima. | Evitar sessões muito lentas e manter experiência mínima de recarga. |
| Faturamento MID certificado | Medidor MID registra consumo com certificação para cobrança ou reembolso. | Associar kWh medido ao usuário, centro de custo, empresa ou condomínio. |
| Chaveamento automático de fase | Modelos trifásicos podem migrar para monofásico quando a potência é baixa. | Otimizar uso de excedente solar sem interromper a sessão. |

## LAN (Ethernet RJ45): canal preferencial para cloud, telemetria e estabilidade

A LAN conecta o carregador ao roteador/switch e, por consequência, ao SEMS cloud. Em instalações com vários carregadores, é a interface recomendada por estabilidade e menor exposição a interferências.

| Parâmetro | Valor / detalhe | Aplicação prática |
|---|---|---|
| Tipo físico | RJ45 com cabo UTP Cat5e ou superior | Cabeamento estruturado para garagens, condomínios e estacionamentos. |
| Alcance | Até 100 m por trecho entre carregador e switch/roteador | Permite concentrar múltiplos pontos em switch dedicado. |
| Destino | Roteador/switch local -> internet -> SEMS cloud GoodWe | Envia telemetria e recebe comandos/configurações via ecossistema GoodWe. |
| IP | DHCP ou IP fixo configurável via SolarGo | IP fixo facilita gestão de rede e troubleshooting. |
| API local | Porta local pode existir, mas não há API local documentada no material analisado | Integração deve priorizar SEMS API ou OCPP, se suportado. |
| Robustez | Alta em comparação ao Wi-Fi | Preferencial para uso comercial, múltiplos carregadores e operação contínua. |

| Função via LAN | O que permite fazer | Uso pela plataforma |
|---|---|---|
| Monitoramento em tempo real | Status, potência atual, energia da sessão, alarmes e modo ativo. | Exibir disponibilidade, consumo, falhas e histórico no painel operacional. |
| Configuração remota de modos | Alteração de Fast, PV Priority e PV+Battery pelo ecossistema GoodWe. | Criar políticas de carga por local, usuário, horário ou energia solar. |
| Agendamento de recarga | Programação de início/fim de sessão. | Oferecer agendamento por tarifa, janela noturna ou regra condominial. |
| Upload de telemetria | Eventos, sessões e consumo sobem para o SEMS. | Sincronizar dados para dashboard, relatórios e cobrança. |
| Integração via API SEMS | Acesso a dados por API para terceiros, conforme autorização GoodWe. | Integração mais direta quando OCPP não estiver disponível. |
| Firmware OTA | Atualizações remotas via conexão de rede. | Manter frota de carregadores atualizada sem visita técnica constante. |

## Wi-Fi 2,4 GHz: alternativa sem fio ao canal LAN

O Wi-Fi oferece as mesmas funções cloud da LAN, mas é mais sensível a distância, paredes, concreto, interferência e saturação de dispositivos. É útil em retrofit ou instalações onde cabo não é viável.

| Parâmetro | Valor / detalhe | Impacto para a plataforma |
|---|---|---|
| Padrão | Wi-Fi 2,4 GHz IEEE 802.11 b/g/n | Compatível com redes comuns, mas sem banda 5 GHz. |
| Faixa de frequência | 2412-2472 MHz | Sujeita a congestionamento em garagens, prédios e locais com muitos dispositivos. |
| Potência máxima | 18,99 dBm (~79 mW) | Alcance depende muito do ambiente. |
| Homologação Brasil | ANATEL nº 06795-24-02673 | Relevante para conformidade de uso no Brasil. |
| Configuração | Via Bluetooth/SolarGo: selecionar SSID, senha, DHCP/IP fixo | A plataforma deve prever etapa de comissionamento presencial. |
| Limitação | Sem 5 GHz e sem interface web local documentada | Evitar como primeira escolha em hubs com muitos carregadores. |

| Critério | LAN | Wi-Fi 2,4 GHz | Decisão recomendada |
|---|---|---|---|
| Estabilidade | Alta, sem interferência de rádio | Média, sujeita a interferência | LAN para operação comercial. |
| Infraestrutura | Exige passagem de cabo | Dispensa cabo | Wi-Fi para retrofit ou vaga isolada. |
| Múltiplos carregadores | Escala bem com switch | Pode saturar canal 2,4 GHz | LAN para hubs e condomínios grandes. |
| Ambiente de concreto | Pouco impacto no cabo | Atenuação significativa | Wi-Fi exige teste de sinal e AP dedicado. |
| Manutenção | Mais previsível | Pode exigir reposicionamento de AP/rede mesh | LAN reduz chamados por instabilidade. |

## Bluetooth BLE: configuração local e manutenção presencial

O Bluetooth Low Energy não deve ser tratado como canal de integração contínua. Ele serve para acesso local do instalador/técnico pelo SolarGo App, principalmente no primeiro comissionamento e em manutenções.

| Parâmetro | Valor / detalhe | Uso pela plataforma |
|---|---|---|
| Padrão | Bluetooth Low Energy (BLE) 1M & 2M | Canal local de baixa potência. |
| Frequência | 2402-2480 MHz | Comunicação curta para smartphone próximo. |
| Potência máxima | 2,99 dBm (~2 mW) | Baixo alcance e baixa exposição; foco em onboarding. |
| Alcance | Até 10 m | Exige presença física do técnico. |
| App | SolarGo (Android/iOS) | Ferramenta de instalação, ajuste e diagnóstico. |
| Senha inicial | goodwe2022, recomendada alteração no primeiro acesso | A plataforma deve guardar procedimento seguro para credenciais por equipamento. |
| Bloqueio | Após 3 tentativas incorretas, pode exigir suporte GoodWe | Importante para checklist de manutenção e gestão de senhas. |

| Função via Bluetooth/SolarGo | O que permite fazer | Quando utilizar |
|---|---|---|
| Configurar Wi-Fi | Selecionar rede, senha, DHCP ou IP fixo. | Instalação inicial, troca de roteador ou correção de conexão. |
| Definir modo de carregamento | Fast, PV Priority, PV+Battery e parâmetros associados. | Comissionamento e ajuste fino da operação. |
| Verificar status de comunicação | Ícones de inversor, medidor MID, Wi-Fi e cloud. | Troubleshooting em campo. |
| Vincular cartões RFID | Associar cartões físicos ao carregador. | Cadastro inicial ou adição/substituição de usuários/cartões. |
| Configurar Dynamic Load Control | Definir corrente máxima permitida da rede. | Unidades com limitação de carga ou risco de sobrecarga. |
| Consultar alarmes | Acessar falhas e eventos localmente. | Manutenção sem depender de acesso ao cloud. |
| Configurar AUTO Start | Permitir início automático ao conectar o cabo. | Uso privado simples, sem controle por usuário. |

## RFID 13,56 MHz: autenticação física do usuário

O RFID é a interface mais relevante para uma experiência de recarga compartilhada sem aplicativo. O usuário aproxima um cartão previamente vinculado e inicia a sessão localmente, desde que o cabo esteja conectado conforme a sequência correta.

| Parâmetro | Valor / detalhe | Uso pela plataforma |
|---|---|---|
| Frequência | 13,56 MHz (NFC) | Cartões de curta distância. |
| Distância de leitura | < 5 cm | Autenticação por aproximação, com baixa chance de leitura acidental. |
| Padrão de cartão | ISO 14443 / Mifare Classic / NFC | Permite cartão físico para usuário, frota ou unidade. |
| Cartões inclusos | 2 cartões RFID na caixa | Suficiente para testes, mas operação comercial exige gestão de cartões. |
| Vinculação | Cartão deve ser vinculado via SolarGo ou SEMS antes do uso | Plataforma precisa mapear cartão -> usuário -> cobrança. |
| Sequência correta | 1º conectar cabo ao VE; 2º aproximar cartão | Reduz falhas operacionais e suporte ao usuário. |
| Roaming | Sem OCPP ativo, cartões de outras redes não funcionam nativamente | Para interoperabilidade real, confirmar OCPP/backend externo. |

| Método de autenticação | Requer internet? | Requer app? | Uso recomendado | Papel da plataforma |
|---|---|---|---|---|
| RFID | Não para iniciar localmente; sim para sincronização cloud | Não | Condomínio, frota, usuário sem smartphone | Vincular cartão a usuário, registrar sessão e faturar. |
| AUTO Start | Não | Não | Vaga privada sem controle de acesso | Não recomendado para uso compartilhado, pois não identifica usuário. |
| App SolarGo/SEMS | Sim | Sim | Usuário com acesso ao ecossistema GoodWe | Útil quando plataforma aceita fluxo GoodWe. |
| Agendamento via app | Sim | Sim | Recarga noturna ou janela tarifária | Pode ser refletido em regras da plataforma, se API permitir. |

# GoodWe SEMS Portal API - Dados Expostos sobre o Carregador HCA G2

Status - Potência - Energia Entregue - Eventos de Sessão

Levantamento baseado em fontes públicas - junho/2026

Resumo executivo: A API SEMS conhecida pela comunidade não expõe tudo que uma plataforma comercial precisa. Ela permite ler status, potência, corrente, modo e energia acumulada, além de enviar comandos de start/stop e modo de carga. Porém, dados como ID do usuário/RFID, histórico estruturado de sessões, energia por sessão pronta e dados MID certificados não aparecem diretamente nos endpoints públicos mapeados.

| Dado principal | Disponível? | Como aparece na API | Uso pela plataforma |
|---|---|---|---|
| Status do carregador | SIM | Campo status: Offline, Standby/Idle, Charging, Fault/Error | Base para saber se o ponto está disponível, em uso ou com falha. |
| Estado do veículo | SIM* | Campo work_status: não plugado, conectado, finalizado. *Há bug conhecido no HCA G2, corrigido no fork WolfrageTV. | Ajuda a detectar conexão/desconexão e fim de sessão. |
| Potência instantânea | SIM | Campo charge_power em W; leitura por polling, tipicamente a cada 60s. | Permite dashboard em tempo real e cálculo de potência média da sessão. |
| Corrente instantânea | SIM | Campo charge_current em A. | Útil para diagnóstico, limite de carga e acompanhamento técnico. |
| Energia entregue | SIM | Campo charge_energy em kWh acumulado total. | A plataforma deve calcular a energia da sessão por delta: fim - início. |
| Eventos de sessão | DERIVADO | Início/fim inferidos por transições de status/work_status. | Não há webhook nem log de sessões pronto; a plataforma precisa armazenar seu próprio histórico. |
| Usuário / RFID | NÃO | Não retornado nos payloads conhecidos. | Crítico para faturamento individual; identidade deve ser gerenciada fora da SEMS API. |

## Arquitetura Geral da SEMS API

A GoodWe oferece diferentes formas de acesso aos dados dos dispositivos. Para o carregador HCA G2, o caminho mais relevante para a plataforma é a OpenAPI/SEMS cloud, usada para leitura de status, telemetria básica e comandos remotos. As APIs de dados em tempo real e controle em lote exigem contrato/whitelist e não substituem, por si só, uma integração padrão para carregadores.

| Tipo de API | Acesso | Função principal | Protocolo | Limite |
|---|---|---|---|---|
| OpenAPI | Conta organizacional SEMS (admin, técnico ou visitante) | Dados processados pelo SEMS: plantas, dispositivos, status, controle remoto e datalogger | HTTPS JSON | 3.600 chamadas/hora por conta |
| Real-time Data Monitoring API | Terceiros com contrato, whitelist e autorização do usuário final | Dados brutos em tempo real, principalmente de inversores; sem controle | HTTPS POST JSON | Definido em contrato |
| Batch Remote Control Interface | Terceiros fornecedores de serviço | Controle remoto em lote, gestão dinâmica de rede e comandos por tópicos | Kafka JSON topics | Definido em contrato |

Autenticação e estabilidade: Toda integração começa por um CrossLogin. A resposta contém o token e o campo api, que define a URL base correta da região. Usar a URL errada costuma gerar erro de autorização expirada. Como os endpoints mapeados pela comunidade podem mudar sem aviso, a plataforma deve implementar renovação de token, retry, timeout e fallback de versão.

```text
POST https://www.semsportal.com/api/v3/Common/CrossLogin
Header: Content-Type: application/json
Header: token: {"version":"","client":"semsPlusAndroid","language":"en"}
Body: {"account":"<email>", "pwd":"<senha>"}

Resposta relevante:
{
 "hasError": false,
 "code": 0,
 "msg": "Successful",
 "data": {
 "uid": "...",
 "timestamp": "...",
 "token": "...",
 "api": "https://eu.semsportal.com/api/"
 }
}

Chamadas seguintes:
Header: token: {"uid":"...", "timestamp":"...", "token":"..."}
```

| Parâmetro operacional | Valor prático | Implicação para a plataforma |
|---|---|---|
| Rate limit padrão | 3.600 chamadas/hora | Equivale à média de 1 chamada por segundo. Polling de 60s suporta cerca de 60 carregadores por conta antes de pressionar o limite. |
| Modelo de atualização | Polling, não push | Eventos de sessão são detectados com atraso igual ao intervalo de polling. |
| Conta recomendada | Visitante SEMS, quando possível | Evita expor credenciais administrativas em integrações de produção. |
| Ambiente regional | URL base retornada no CrossLogin | A plataforma deve gravar e usar o endpoint regional retornado no token. |

## Endpoints do carregador EV e dados expostos 

Os endpoints abaixo foram identificados em integrações open source e discussões técnicas. Eles não aparecem integralmente na documentação pública oficial, por isso devem ser tratados como mapeamento operacional sujeito a mudanças.

| Endpoint | Método / caminho | Dados retornados | Uso pela plataforma |
|---|---|---|---|
| Status principal v3 | POST /api/v3/EvCharger/GetCurrentChargeinfo | Leitura atual do carregador: status, work_status, charge_power, charge_energy, charge_current, charge_mode e número de série. | Endpoint mais importante para dashboard e controle operacional. |
| Status ampliado v4 | POST /api/v4/EvCharger/GetEvChargerMoreView | Visão ampliada do carregador no SEMS+, com mais campos quando disponível. | Recomendado tentar v4 primeiro e fazer fallback para v3 se retornar 404. |
| Detalhe da planta | GET /powerstation/EvChargerDetail?stationId={station_id} | Dados do carregador agregados ao contexto da planta FV, incluindo isEvCharge e evCharge quando disponíveis. | Útil quando a plataforma organiza carregadores por planta/estação solar. |

```text
POST /api/v3/EvCharger/GetCurrentChargeinfo
Request: {"sn":"<serial_do_carregador>"}

Resposta - campos relevantes:
{
 "hasError": false,
 "code": 0,
 "msg": "Successful",
 "data": {
 "status": 2, // estado operacional geral
 "work_status": 1, // estado de conexão do veículo
 "charge_power": 7400, // potência instantânea em W
 "charge_energy": 123.45, // energia total acumulada em kWh
 "charge_current": 32, // corrente instantânea em A
 "charge_mode": 0, // modo Fast/PV/PV+Battery
 "sn": "..." // número de série
 }
}
```

Boa prática de integração: Para uso comercial, a plataforma deve persistir cada leitura recebida com timestamp próprio. Isso permite reconstruir sessões, calcular energia entregue por sessão, montar gráficos de potência e auditar indisponibilidades mesmo quando a SEMS API não fornece eventos estruturados.

## Status do Carregador: o que a API expõe

Os campos de status indicam se o carregador está online, parado, carregando, em falha e se o veículo está conectado ao cabo. Eles são a base para disponibilidade do ponto, abertura/encerramento de sessão e alertas operacionais.

| Campo JSON | Tipo | Valores conhecidos | Descrição | Como usar na plataforma |
|---|---|---|---|---|
| status | integer | 0 = Offline<br>1 = Standby / Idle<br>2 = Charging<br>3 = Fault / Error | Estado operacional geral do carregador. | Disponibilidade do ponto, alerta de falha, início e fim de sessão por transição de estado. |
| work_status | integer | 0 = Not Plugged In<br>1 = Connected (EV plugged)<br>2 = Finished Charging | Estado de conexão do veículo ao conector. Há bug conhecido no HCA G2 em integrações antigas. | Detectar plug conectado, veículo finalizado e possíveis falsos negativos; usar correção do fork WolfrageTV. |
| charge_mode | integer | 0 = Fast<br>1 = PV Priority<br>2 = PV & Battery | Modo de carga ativo configurado no carregador. | Exibir modo atual e auditar alterações feitas pela plataforma ou pelo app SEMS. |
| sn | string | Número de série | Identificador único do carregador no SEMS. | Chave primária para associar leituras, comandos, localização e cadastro na plataforma. |

| Transição observada | Interpretação operacional | Ação recomendada na plataforma |
|---|---|---|
| status 1 -> 2 | Início provável de sessão de carga. | Criar sessão pendente/ativa com timestamp do poll e charge_energy inicial. |
| status 2 -> 1 | Fim provável de sessão de carga. | Encerrar sessão e calcular energia: charge_energy final - inicial. |
| status qualquer -> 3 | Falha ou erro no carregador. | Gerar alerta, bloquear início de novas sessões e registrar evento de manutenção. |
| work_status 0 -> 1 | Veículo plugado. | Marcar conector ocupado fisicamente, mesmo antes de carregar. |
| work_status 1 -> 2 | Carga finalizada pelo veículo ou carregador. | Validar encerramento e aguardar estabilização para evitar falso evento. |

Atenção: Como a API trabalha por polling, o timestamp real do evento pode ocorrer entre duas leituras. Com polling de 60 segundos, a precisão prática do início/fim da sessão é de aproximadamente +/- 60 segundos. Para cobrança por minuto ou por segundo, isso precisa estar previsto na regra comercial.

## Potência, corrente e energia entregue

A API expõe dados suficientes para telemetria básica do carregador: potência instantânea, corrente instantânea e energia acumulada total. O ponto mais importante é que a energia por sessão não vem pronta; ela precisa ser calculada pela plataforma.

| Campo API | Tipo | Unidade | O que representa | Uso pela plataforma |
|---|---|---|---|---|
| charge_power | float | W | Potência instantânea de carga. Normalmente zero quando não está carregando. | Gráfico em tempo real, potência média da sessão, diagnóstico de redução de carga. |
| charge_current | float | A | Corrente instantânea de carga. Restaurada/corrigida em forks para HCA G2. | Diagnóstico técnico, checagem de corrente esperada e suporte a limites operacionais. |
| charge_power (limite) | float | kW | Limite de potência configurável no modo Fast, via comando SetChargeMode. | Controle dinâmico de potência por plano, horário, demanda ou limite contratado. |
| charge_energy | float | kWh | Energia total entregue acumulada pelo carregador desde instalação ou último reset. | Base para calcular energia por sessão por diferença entre leitura inicial e final. |

Regra de faturamento: charge_energy é acumulado total, não energia da sessão atual. Para cada sessão, salve charge_energy no início e no fim: energia_sessao = charge_energy_final - charge_energy_inicial. Se a API falhar no encerramento, use a última leitura válida antes do fim e marque a sessão como estimada.

| Indicador calculado pela plataforma | Fórmula / lógica | Observação |
|---|---|---|
| Energia da sessão (kWh) | charge_energy_fim - charge_energy_inicio | Acurado se as leituras inicial e final forem capturadas corretamente. |
| Potência média da sessão | média dos valores de charge_power durante a sessão | É uma média amostrada pelo intervalo de polling, não uma medição contínua. |
| Pico de potência | max(charge_power) durante a sessão | Pode perder picos curtos se o polling for lento. |
| Tempo conectado | timestamp desconexão - timestamp conexão | Depende de work_status; aplicar filtros contra falsos positivos. |
| Tempo carregando | timestamp fim charging - timestamp início charging | Base para cobrança por tempo ativo, com precisão limitada pelo polling. |

## Eventos de Sessão: o que expõe, o que é derivado e o que falta 

A maior limitação da API SEMS para plataformas de recarga compartilhada está nos eventos de sessão. A API não entrega um histórico estruturado de sessões com usuário, cartão RFID, início, fim e energia consumida. A plataforma precisa montar esse histórico a partir das leituras de status e energia acumulada.

| Evento / dado | Disponível? | Como obter | Limitação |
|---|---|---|---|
| Início da sessão | DERIVADO | Transição status 1 -> 2; registrar timestamp do poll. | Precisão limitada pelo intervalo de polling. |
| Fim da sessão | DERIVADO | Transição status 2 -> 1 ou work_status -> 2. | Usar grace period para evitar flickering/falso encerramento. |
| Energia da sessão | DERIVADO | charge_energy(fim) - charge_energy(início). | Não existe campo direto de energia por sessão no endpoint v3/v4 conhecido. |
| Potência média | DERIVADO | Média dos valores charge_power lidos durante a sessão. | Amostrada; não captura todos os picos e vales. |
| Estado do veículo | SIM | work_status: não conectado, conectado, finalizado. | Campo teve bug em HCA G2; validar implementação. |
| Usuário / RFID | NÃO | Não retornado nos payloads conhecidos. | Identidade deve vir da plataforma, do app próprio, do backend OCPP ou de outro controle externo. |
| Histórico de sessões | NÃO | Não há lista paginada pública conhecida. | A plataforma precisa armazenar log próprio de sessões. |

| Dado ausente | Impacto na plataforma | Alternativa possível |
|---|---|---|
| ID do usuário ou cartão RFID | Sem esse dado, não há como saber quem carregou apenas pela SEMS API. | Autenticar o usuário no app da plataforma e acionar start/stop pela API; ou confirmar OCPP/backend externo. |
| Histórico estruturado de sessões | Sem relatório nativo de sessões para auditoria e faturamento. | Criar banco próprio com leituras periódicas, transições, comandos e deltas de energia. |
| Custo por sessão | API entrega energia, não preço final. | Calcular internamente por tarifa, plano, local, horário e impostos. |
| Webhooks de evento | A plataforma só detecta eventos no próximo poll. | Ajustar polling conforme criticidade e respeitar rate limit. |
| Dados MID certificados via cloud | Não há exposição conhecida do medidor MID pela SEMS API. | Ler o MID localmente via Modbus/RS-485 quando for necessário dado certificado. |
| SOC do veículo | HCA G2 AC Tipo 2 não fornece SOC do VE via SEMS. | Integrar diretamente com APIs do veículo quando disponível. |

## Comandos remotos e relação com os dados

Além da leitura de dados, a SEMS API permite comandos remotos identificados pela comunidade. Eles são úteis para uma plataforma que autentica o usuário fora da GoodWe e depois controla o carregador: iniciar, parar, definir modo e ajustar limite de potência.

| Comando | Endpoint | Payload principal | Restrição conhecida |
|---|---|---|---|
| Iniciar recarga | POST /api/v3/EvCharger/Charging | {"sn":"...", "status":"1"} | No HCA G2, usar sequência recomendada stop -> set_mode -> start para evitar bug. |
| Parar recarga | POST /api/v3/EvCharger/Charging | {"sn":"...", "status":"0"} | Aplicar grace period após comando para evitar alternância visual/falso estado. |
| Definir modo Fast | POST /api/v3/EvCharger/SetChargeMode | {"sn":"...", "type":0, "charge_power":7.4} | charge_power é obrigatório/relevante apenas no modo Fast. |
| Definir PV Priority | POST /api/v3/EvCharger/SetChargeMode | {"sn":"...", "type":1} | Limite de potência passa a depender do inversor/surplus FV. |
| Definir PV+Battery | POST /api/v3/EvCharger/SetChargeMode | {"sn":"...", "type":2} | Requer inversor e bateria conectados via RS-485. |
| Ler status atual | POST /api/v3/EvCharger/GetCurrentChargeinfo | {"sn":"..."} | Polling padrão de 60s; não há webhook/push. |

Uso na plataforma: O comando de start/stop é associado ao carregador, não ao usuário. Portanto, se a plataforma quer faturar por usuário, ela precisa registrar internamente qual usuário autenticou, qual comando foi enviado, em qual carregador e em qual timestamp. A API SEMS não resolve essa identidade sozinha.

Fluxo recomendado para sessão controlada pela plataforma:

1. Usuário autentica no app / QR Code / RFID próprio da plataforma.
2. Plataforma valida permissão e saldo/plano.
3. Plataforma salva charge_energy_inicial e timestamp_inicio.
4. Plataforma envia comando de start.
5. Plataforma faz polling de status, charge_power, charge_current e charge_energy.
6. No fim, envia stop ou detecta fim por status/work_status.
7. Plataforma salva charge_energy_final e calcula kWh da sessão.
8. Plataforma calcula custo, grava recibo e libera relatório.

# EV ChargeOps — Frente 3: Arquitetura e IA

---

## Camadas da Plataforma EV ChargeOps

A plataforma é organizada em quatro camadas interdependentes:

**Camada física** — o carregador GoodWe HCA G2 instalado no estacionamento L1 da FIAP (Aclimação). É o ponto de origem de todos os dados operacionais: potência instantânea, energia entregue (kWh), status da sessão e identidade do usuário via RFID.

**Camada de conectividade** — responsável por transportar os dados do carregador até o back-end. O HCA G2 suporta LAN, Wi-Fi, RS-485 e Bluetooth. Para a plataforma, a comunicação principal ocorre via LAN/Wi-Fi com integração à API SEMS Portal da GoodWe (HTTPS + JSON). O protocolo RS-485 pode ser usado para integração local direta em cenários sem conectividade de rede confiável.

**Camada de aplicação** — back-end em Python responsável por: ingerir os dados da API SEMS, persistir as sessões em banco relacional (PostgreSQL), executar as regras de rateio e acionar os módulos de IA para análise e predição. É aqui que ocorre toda a lógica de negócio.

**Camada de apresentação** — duas interfaces distintas: um painel do gestor (visualização agregada, relatórios, alertas, configuração de regras de rateio) e uma interface do usuário/morador (histórico de sessões pessoais, consumo do mês, valor estimado da fatura).

---

## Fluxo de Dados: da Sessão à Fatura

O caminho completo percorre seis etapas:

1. **Conexão do veículo** — o usuário se autentica via RFID no HCA G2. O carregador abre uma sessão e começa a registrar potência (kW) e energia entregue (kWh) em intervalos regulares.

2. **Exposição via API SEMS** — a GoodWe disponibiliza os dados da sessão pelo endpoint `EvChargerDetail` do SEMS Portal. Os campos retornados incluem `evChargerStatus`, `power` (kW instantâneo), energia acumulada da sessão e timestamps de início e fim. O formato é JSON autenticado via token Bearer (obtido em `Auth/GetToken`).

3. **Ingestão e persistência** — o back-end Python consome a API em intervalos periódicos (polling), normaliza os dados e os grava na tabela `sessoes` do banco. Cada registro armazena: `id_sessao`, `id_usuario`, `id_unidade`, `inicio`, `fim`, `kwh_entregues`, `status`.

4. **Aplicação das regras de rateio** — ao encerrar o mês, o módulo de rateio agrega o consumo por unidade, aplica o modelo escolhido (detalhado na Opção A abaixo) e gera os registros na tabela `faturas`.

5. **Enriquecimento por IA** — antes de fechar a fatura, os módulos de IA (detalhados na Opção B) anotam a sessão com perfil de uso, sinalizam anomalias e atualizam as previsões de consumo futuro.

6. **Apresentação** — os dados de fatura e histórico ficam disponíveis nas interfaces do gestor e do usuário.

---

## Modelo de Rateio Proposto

### Opção A — Benchmarking de modelos de rateio

Dois modelos foram identificados e analisados:

**Modelo 1 — Rateio proporcional por kWh consumido (cobrança individualizada)**

Cada usuário paga exatamente o que consumiu. O custo unitário é calculado dividindo o valor total da fatura de energia elétrica do condomínio (ou do quadro dedicado aos carregadores) pelo total de kWh entregues no período.

```
Custo_unitário = Valor_fatura_total (R$) / Total_kWh_entregues
Fatura_usuário = Custo_unitário × kWh_consumidos_pelo_usuário
```

Vantagens: justiça direta, sem subsídio cruzado entre usuários, fácil de auditar.  
Limitações: exige medição confiável por sessão/usuário; não reflete picos de demanda que oneram a tarifa de forma não-linear.

**Modelo 2 — Rateio por fundo condominial com cota fixa + variável**

O condomínio estima um custo fixo mensal de infraestrutura (manutenção, depreciação do carregador, taxa de gestão) rateado igualmente entre todos os usuários cadastrados, e uma parcela variável cobrada por kWh consumido.

```
Fatura_usuário = (Custo_fixo_mensal / nº_usuários_ativos) + (Custo_variável × kWh_usuário)
```

Vantagens: cobre custos de manutenção independentemente do volume de uso; previsível para o gestor.  
Limitações: penaliza usuários de baixo consumo; maior resistência em assembleia.

**Modelo adotado pela equipe: Modelo 1 — rateio proporcional por kWh**

A decisão se justifica pela compatibilidade com o princípio regulatório da ANEEL (cobrança pelo consumo efetivo), pela simplicidade de auditoria e por não onerar usuários que carregaram pouco no mês. A plataforma registra cada kWh entregue por sessão/usuário, o que torna o cálculo diretamente verificável.

**Tratamento de casos excepcionais:**

- **Sessão interrompida:** registrada com o kWh efetivamente entregue até o momento da interrupção. O valor cobrado é proporcional ao consumo real, não à sessão completa.
- **Usuário que não carregou no mês:** não recebe fatura. O denominador do rateio considera apenas usuários com consumo > 0 kWh no período.
- **Dois veículos da mesma unidade:** ambos os veículos são cadastrados sob o mesmo `id_unidade`. O consumo é somado e a fatura é emitida por unidade, não por veículo. O gestor pode optar por detalhar por veículo no relatório sem alterar o cálculo da fatura.

---

## Papel da IA na Solução

### Opção B — Definição do papel da IA

Duas abordagens foram identificadas, pesquisadas e definidas para integração na plataforma:

---

#### Abordagem 1 — Clustering para perfis de uso (K-Means)

**Problema que resolve:** o gestor não sabe quem são os usuários de alta frequência, quem carrega em horários de pico e quem usa o carregador de forma esporádica. Sem essa visão, é impossível criar políticas de agendamento, priorização ou incentivos diferenciados.

**Técnica:** K-Means clustering aplicado às sessões históricas. Cada sessão é representada por um vetor de features: duração, kWh entregues, horário de início, dia da semana e frequência mensal do usuário. O algoritmo agrupa usuários em perfis comportamentais.

**Dados necessários:** tabela `sessoes` com ao menos 2-3 meses de histórico, campos `inicio`, `fim`, `kwh_entregues`, `id_usuario`.

**Implementação em Python:**
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# features: duracao_min, kwh, hora_inicio, dia_semana, freq_mensal
X = df[['duracao_min', 'kwh_entregues', 'hora_inicio', 'dia_semana', 'freq_mensal']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
df['perfil'] = kmeans.fit_predict(X_scaled)
```

**Impacto esperado:** geração automática de perfis como "carregador noturno intensivo", "uso esporádico diurno" e "carregador em horário de pico". O gestor visualiza esses perfis no painel e pode criar regras de agendamento ou tarifas diferenciadas por horário.

**Referência técnica:** estudos com K-Means em dados de carregamento EV identificaram até 6 arquétipos comportamentais distintos com F1-macro acima de 0,99, demonstrando alta separabilidade dos perfis no espaço de features operacionais.

---

#### Abordagem 2 — Detecção de anomalias com Isolation Forest

**Problema que resolve:** sessões com comportamento atípico — consumo anormalmente alto, duração inconsistente com a energia entregue, ou padrões que sugerem falha no carregador ou fraude — passam despercebidas sem um mecanismo automatizado de detecção.

**Técnica:** Isolation Forest, algoritmo não supervisionado que isola outliers construindo árvores de decisão aleatórias. Pontos que exigem poucas partições para serem isolados são classificados como anômalos. Adequado para dados de sessão porque não requer rótulos de treino e é robusto a distribuições não-normais.

**Dados necessários:** tabela `sessoes` com campos numéricos de cada sessão (`kwh_entregues`, `duracao_min`, `potencia_media_kw`). Não requer dados rotulados.

**Implementação em Python:**
```python
from sklearn.ensemble import IsolationForest

features = df[['kwh_entregues', 'duracao_min', 'potencia_media_kw']]
iso = IsolationForest(contamination=0.02, random_state=42)
df['anomalia'] = iso.fit_predict(features)
# -1 = anômalo, 1 = normal

anomalias = df[df['anomalia'] == -1]
```

**Impacto esperado:** o sistema sinaliza automaticamente sessões suspeitas para revisão do gestor antes de fechar a fatura. Reduz erros de cobrança, detecta falhas no equipamento precocemente e cria um log de eventos para auditoria. Estudos aplicados a redes de carregamento real identificaram anomalias em 0,67% a 2,36% das sessões, demonstrando que o volume de falsos alertas é administrável.

**Limitação conhecida:** Isolation Forest pode classificar incorretamente eventos legítimos raros (ex: primeira sessão de um usuário) como anômalos. A plataforma trata isso exibindo as anomalias como "sugestões de revisão", não como bloqueios automáticos.

---

### Resumo do papel da IA no fluxo

| Módulo | Técnica | Quando executa | Saída |
|---|---|---|---|
| Perfis de uso | K-Means | Processamento mensal em batch | Tag de perfil por usuário |
| Detecção de anomalias | Isolation Forest | A cada nova sessão encerrada | Flag `anomalia` na tabela `sessoes` |

---

## Opção C — Esquema da Base de Dados

### Entidades e atributos

**Tabela `usuarios`**

| Campo | Tipo | Descrição |
|---|---|---|
| id_usuario | UUID (PK) | Identificador único do usuário |
| nome | VARCHAR(100) | Nome completo |
| email | VARCHAR(150) | E-mail de contato |
| rfid_tag | VARCHAR(50) | Tag RFID vinculada ao usuário |
| id_unidade | INTEGER (FK) | Unidade condominial do usuário |
| ativo | BOOLEAN | Indica se o cadastro está ativo |
| criado_em | TIMESTAMP | Data de cadastro |

**Tabela `unidades`**

| Campo | Tipo | Descrição |
|---|---|---|
| id_unidade | INTEGER (PK) | Identificador da unidade |
| numero | VARCHAR(20) | Número do apartamento/sala |
| bloco | VARCHAR(10) | Bloco ou torre |
| tipo | VARCHAR(30) | residencial / corporativo / universitário |

**Tabela `sessoes`**

| Campo | Tipo | Descrição |
|---|---|---|
| id_sessao | UUID (PK) | Identificador único da sessão |
| id_usuario | UUID (FK) | Usuário que iniciou a sessão |
| id_unidade | INTEGER (FK) | Unidade associada |
| inicio | TIMESTAMP | Momento de conexão do veículo |
| fim | TIMESTAMP | Momento de desconexão (NULL se em andamento) |
| kwh_entregues | DECIMAL(8,3) | Energia efetivamente entregue |
| potencia_media_kw | DECIMAL(6,3) | Potência média da sessão |
| duracao_min | INTEGER | Duração em minutos |
| status | VARCHAR(20) | concluída / interrompida / em_andamento |
| anomalia | BOOLEAN | Flag gerada pelo módulo de IA |
| perfil_uso | VARCHAR(30) | Perfil atribuído pelo clustering (nullable) |
| fonte_dados | VARCHAR(30) | sems_api / rs485 / manual |

**Tabela `faturas`**

| Campo | Tipo | Descrição |
|---|---|---|
| id_fatura | UUID (PK) | Identificador único da fatura |
| id_unidade | INTEGER (FK) | Unidade faturada |
| periodo_inicio | DATE | Início do período de referência |
| periodo_fim | DATE | Fim do período de referência |
| kwh_total | DECIMAL(8,3) | Total consumido pela unidade no período |
| custo_unitario | DECIMAL(10,4) | R$/kWh calculado para o período |
| valor_total | DECIMAL(10,2) | Valor em R$ a ser cobrado |
| gerada_em | TIMESTAMP | Quando a fatura foi gerada |
| status | VARCHAR(20) | pendente / emitida / paga |

---

### Relacionamentos

```
unidades 1 ──< usuarios (uma unidade pode ter vários usuários)
usuarios 1 ──< sessoes  (um usuário tem várias sessões)
unidades 1 ──< sessoes  (uma unidade acumula várias sessões)
unidades 1 ──< faturas  (a fatura é emitida por unidade)
```

---

### Exemplos de registros simulados

**usuarios**
```
id_usuario: 'a1b2c3d4-...'  |  nome: 'Carlos Lima'  |  rfid_tag: 'RFID-00421'  |  id_unidade: 7  |  ativo: true
```

**sessoes**
```
id_sessao: 'e5f6...'  |  id_usuario: 'a1b2...'  |  inicio: '2026-06-10 19:32:00'  |  fim: '2026-06-10 22:15:00'
kwh_entregues: 18.740  |  potencia_media_kw: 7.04  |  duracao_min: 163  |  status: 'concluída'  |  anomalia: false
```

**faturas**
```
id_fatura: 'f7g8...'  |  id_unidade: 7  |  periodo: jun/2026  |  kwh_total: 54.320
custo_unitario: 0.9814  |  valor_total: 53.29  |  status: 'pendente'
```

O valor de `custo_unitario` é recalculado mensalmente com base no valor real da fatura de energia do quadro dedicado dividido pelo total de kWh entregues no período, conforme o modelo de rateio proporcional adotado.

---

## Plano para a Sprint 02

Na Sprint 02, a equipe implementará a plataforma em Python com a seguinte ordem de desenvolvimento:

1. **Módulo de ingestão** — script Python que consome a API SEMS via polling, normaliza os dados e persiste na tabela `sessoes` (PostgreSQL com SQLAlchemy).
2. **Motor de rateio** — função que agrega consumo por unidade ao fim do período e gera registros na tabela `faturas` com o modelo proporcional por kWh.
3. **Módulo de IA** — pipeline scikit-learn com Isolation Forest (detecção de anomalias) e K-Means (perfis de uso), executado como job batch mensal.
4. **API REST** — FastAPI expondo endpoints para o painel do gestor e a interface do usuário (consulta de sessões, faturas e alertas de anomalia).
5. **Interface mínima** — dashboard simples (Streamlit ou HTML estático) para visualização das sessões e faturas.

Tecnologias: Python 3.11, FastAPI, SQLAlchemy, PostgreSQL, scikit-learn, pandas, requests (consumo da API SEMS).

# Referências

- Associação Brasileira dos Veículos Elétricos - Eletrificados seguem em ritmo intenso em abril e atingem 16% de participação de mercado:
https://abve.org.br/vendas-de-eletrificados-seguem-em-ritmo-intenso-e-atingem-16-de-participacao-de-mercado-em-abril/
- Agência Nacional de Energia Elétrica - Veículos Elétricos:
https://www.gov.br/aneel/pt-br/assuntos/veiculos-eletricos
- International Energy Agency - Eletric vehicle charging:
https://www.iea.org/reports/global-ev-outlook-2025/electric-vehicle-charging
- International Energy Agency - Global EV Outlook 2025:
https://www.iea.org/reports/global-ev-outlook-2025
- U.S. Department of Energy - Alternative Fuel Data Center - Operation and Mainenance for Electric Vehicle Chargin:
https://afdc.energy.gov/fuels/electricity-infrastructure-maintenance-and-operation
- EVgo Fast Charging - Discover Pricing on the Go:
https://www.evgo.com/pricing/
- eMabler - Pricing models for EV charging: kWh, time-based, and dynamic pricing:
https://emabler.com/resource/pricing-models-for-ev-charging
- Zaptec - Zaptec Pro:
https://www.zaptec.com/charging-solutions/business-and-commercial/zaptec-pro 
- Zaptec - Zaptec Portal: 
https://www.zaptec.com/charging-solutions/zaptec-portal
- Wallbox - Pulsar Plus:
https://wallbox.com/en_us/pulsar-plus-ev-charger
- Chargepoint - Intelligent, flexible EV charging software:
https://www.chargepoint.com/products/software
- NeoCharge - Carregador para Carro Elétrico em Prédios e Condomínios: O que saber antes de instalar: 
https://www.neocharge.com.br/tudo-sobre/carregador-carro-eletrico-predio-condominio-instalacao
- RN ANEEL nº 1.000/2021: https://www.gov.br/aneel/pt-br/assuntos/campanhas/resolucao-1000-da-aneel-seus-direitos-sobre-energia-eletrica-agora-num-so-lugar-2022
- RN ANEEL nº 819/2018: https://www.gov.br/aneel/pt-br/assuntos/veiculos-eletricos
- Lei Estadual SP nº 18.403/2026 - Assembleia Legislativa do Estado de São Paulo: https://www.al.sp.gov.br/repositorio/legislacao/lei/2026/lei-18403-18.02.2026.html
- Decreto Estadual SP nº 69.118/2024 - Assembleia Legislativa do Estado de São Paulo:
https://www.al.sp.gov.br/repositorio/legislacao/decreto/2024/decreto-69118-09.12.2024.html
- Portaria CCB nº 003/970/2026: Diário Oficial do Estado de São Paulo: https://doe.sp.gov.br/executivo/secretaria-da-seguranca-publica/portaria-n-003-970-2026-de-17-de-marco-de-2026-20260316113816712141709068
- Portarias CCB-008/009 800/2025: https://legislacao.prefeitura.sp.gov.br/lei-17336-de-30-de-marco-de-2020
- Lei Municipal SP nº 18.229/2025: https://legislacao.prefeitura.sp.gov.br/lei-18229-de-16-de-janeiro-de-2025
- Norma Enel CNC-OMBR-MAT-19-0280-EDBR: Especificação técnica: Conexão de Recarga para Veículos Elétricos: https://www.eneldistribuicao.com.br/rj/documentos/CNC-OMBR-MAT-19-0280-EDBR%20-%20Conex%C3%A3o%20de%20Recarga%20para%20Ve%C3%ADculos%20El%C3%A9tricos.pdf
- SEFAZ-SP RC 31007/2024: https://legislacao.fazenda.sp.gov.br/Paginas/RC30579_2024.aspx
- Lei Complementar nº 214/2025: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
- GoodWe SEMS Portal API — documentação técnica da comunidade GoodWe: https://community.goodwe.com/static/images/2024-08-20597794.pdf
- Integração SEMS com Home Assistant (discussão de endpoint EvChargerDetail): https://github.com/TimSoethout/goodwe-sems-home-assistant/discussions/179
- pygoodwe — biblioteca Python para acesso à API SEMS: https://pypi.org/project/pygoodwe/
- Binod Karunanayake, "Accessing GoodWe Sems Portal API": https://binodmx.medium.com/accessing-the-goodwe-sems-portal-api-a-comprehensive-guide-296e0431c285
- VAGA55 — modelo de carregamento compartilhado em condomínios: https://www.vaga55.com.br
- Ambare — guia de carregamento compartilhado e rateio: https://ambare.com.br
- EnergySpot — modelos de cobrança em condomínios: https://www.energyspot.com.br
- Neocharge — carregadores em prédios e condomínios: https://www.neocharge.com.br
- Vox e Power — carregamento de VEs em condomínios: https://www.voxepower.com
- Zangari — carros elétricos em condomínio, modelos de rateio (2026): https://zangari.com.br/blog/carros-eletricos-condominio/
- Heliou et al., "Machine learning approaches for the prediction of public EV charge point flexibility", ScienceDirect (2025): https://www.sciencedirect.com/science/article/pii/S2352467725000396
- Matrone et al., "AI-powered anomaly detection and load forecasting for sustainable EV charging networks", ScienceDirect (2026): https://www.sciencedirect.com/science/article/pii/S2352484726001551
- "Behavioral Clustering and Load Characterization of EV Charging Stations using Machine Learning", Processes MDPI (2025): https://doi.org/10.3390/pr14111692
- "Anomaly Detection in Electric Vehicle Charging Stations Using Federated Learning", arXiv (2025): https://arxiv.org/html/2509.18126v1
- "Prediction of EV Charging Behavior Using Machine Learning", ResearchGate: https://www.researchgate.net/publication/353749744