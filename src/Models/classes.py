from owlready2 import get_ontology, Thing, rdfs

cdo_onto = get_ontology("https://onto.colossi.network/cdo")
cdo = cdo_onto.get_namespace("https://onto.colossi.network/cdo#")

with cdo:
    class CDOThing(Thing):
        pass
    rdfs.comment[CDOThing] = ["CDOThing is the top CDO class."]

    class Disposition(CDOThing):
        pass

    #######################################
    class Behaviour(Disposition):
        pass

    class Mereology(CDOThing):
        pass


    class Perspective(Disposition):
        pass

    class Subjective(Perspective):
        pass

    class Objective(Perspective):
        pass

    class Stemmatic(Behaviour):
        pass

    class Systematic(Behaviour):
        pass

    # Object ###############################
    class Structure(Mereology):
        pass

    class Form(CDOThing):
        pass

    class hasForm(Structure >> Form):
        pass

    class Morphological(CDOThing):
        pass

    class Systemic(Mereology):
        pass

    class Passive(Behaviour):
        pass

    class Object(Passive, Systemic, Morphological, Structure):
        pass

    class Text(CDOThing):
        pass

    class hasTexttual(Object >> Text):
        pass

    class Schema(CDOThing):
        pass

    class hasSchema(Object >> Schema):
        pass

    class Attribute(CDOThing):
        pass
    class hasAttributes(Schema >> Attribute):
        pass

    

    # Event ###############################

    class Causable(Disposition):
        pass

    class Active(Behaviour):
        pass

    class Event(Causable, Stemmatic, Active):
        pass

    class Topology(Mereology):
        pass

    class Record(CDOThing):
        pass

    class hasRecord(Event >> Record):
        pass

    class LogEntry(CDOThing):
        pass

    class hasLogEntry(Event >> LogEntry):
        pass

    class Log(CDOThing):
        pass

    class inLog(LogEntry >> Log):
        pass

    class Field(CDOThing):
        pass

    class hasField(Event >> Field):
        pass

    class isTracaebleIn(LogEntry >> Topology):
        pass

    class auditedBy(Log >> Topology):
        pass


    # Concept #############################
    class Epistemic(CDOThing):
        pass
    
    class Concept(Subjective, Epistemic):
        pass

    class Observation(CDOThing):
        pass

    class fromObservation(Epistemic >> Observation):
        pass

    class Context(CDOThing):
        pass
    class hasContext(Concept >> Context):
        pass

    class Notice(CDOThing):
        pass

    class hasNotice(Concept >> Notice):
        pass

    class Literal(CDOThing):
        pass

    class hasTerm(Concept >> Literal):
        pass

    class Frame(CDOThing):
        pass

    class hasFrame(Concept >> Frame):
        pass

    class Knowledge(Mereology):
        pass
    rdfs.comment[Knowledge] = ["A Knowledge Graph that stores wat is known by the agent about the Concept."]

    class nodeIn(Concept >> Knowledge):
        pass

    # Action ###############################
    class Action(Systematic, Objective):
        pass

    class Packet(CDOThing):
        pass

    class hasPacket(Action >> Packet):
        pass

    class Payload(CDOThing):
        pass
    class hasPayload(Packet >> Payload):
        pass

    class Value(CDOThing):
        pass

    class hasPayloadValue(Payload >> Value):
        pass

    class Fact(CDOThing):
        pass
    rdfs.comment[Fact] = ["A Value is factual once a Packet's ACK is received."]

    class isFactual(Action >> Fact):
        pass

    class hasValuePart(Fact >> Value):
        pass 


    class Intelligence(CDOThing):
        # todo
        pass

    class HumanIntelligence(Intelligence):
        pass

    class ArtificialIntelligence(Intelligence):
        pass

    class hasIntelligence(Action >> Intelligence):
        pass

    class causedBy(Event >> Action):
        pass

    # Data #####################################
    class Data(CDOThing):
        pass

    class capturedBy(Data >> Object):
        pass

    class centeredBy(Data >> Event):
        pass

    class accessedAs(Data >> Concept):
        pass

    class exchangedIn(Data >> Packet):
        pass

    class recordOf(Record >> Data):
        pass

    # ConsensualScheme ########################
    class ConsensualScheme(Mereology):
        pass

    class hasConsensualScheme(Data >> ConsensualScheme):
        pass

    class Consensus(CDOThing):
        pass

    class Scheme(Mereology):
        pass

    class hasConsensusOnSubSchema(Schema >> Scheme):
        pass

    class hasConsensus(ConsensualScheme >> Consensus):
        pass

    class hasScheme(ConsensualScheme >> Scheme):
        pass

    class hasConcept(ConsensualScheme >> Concept):
        pass

    class hasConsensusOnSubGraphOf(Knowledge >> Scheme):
        pass

    # SovereignReason ##########################
    class SovereignReason(CDOThing):
        pass

    class Agent(CDOThing):
        pass

    class Sovereignity(CDOThing):
        pass

    class Reason(CDOThing):
        pass

    class sovereignBy(SovereignReason >> Sovereignity):
        pass

    class forEvent(SovereignReason >> Event):
        pass

    class hasSovereignity(Agent >> Sovereignity):
        pass

    class hasReason(SovereignReason >> Reason):
        pass