from owlready2 import get_ontology, Thing, rdfs

cdo_onto = get_ontology("https://onto.colossi.network/cdo")
cdo = cdo_onto.get_namespace("https://onto.colossi.network/cdo#")

with cdo:
    class CDOThing(Thing):
        pass
    rdfs.comment[CDOThing] = ["CDOThing is the top CDO class."]

    #======================================
    class Behaviour(CDOThing):
        pass
    class Passive(Behaviour):
        pass
    class Active(Behaviour):
        pass

    class Perspective(CDOThing):
        pass
    class Objective(Perspective):
        pass
    class Subjective(Perspective):
        pass
    #######################################
    class Object(Passive):
        pass

    class Attribute(CDOThing):
        pass

    class isDefinedBy(Object >> Attribute):
        pass

    class Form(CDOThing):
        pass
    class hasForm(Attribute >> Form):
        pass

    class Schema(CDOThing):
        pass
    class isSystemic(Form >> Schema):
        pass
    class hasAttributes(Schema >> Attribute):
        pass
    class Text(CDOThing):
        pass
    class isTextual(Schema >> Text):
        pass

    #######################################
    class Event(Objective):
        pass

    class Field(CDOThing):
        pass
    class occursIn(Event >> Field):
        pass

    class Log(CDOThing):
        pass
    class isLogged(Field >> Log):
        pass

    class Record(CDOThing):
        pass
    class isStemmatic(Log >> Record):
        pass

    class Track(CDOThing):
        pass
    class isTractual(Record >> Track):
        pass


    #------------------------------
    class Stemma(CDOThing):
        pass
    class underpins(Text >> Stemma):
        pass
    class hasLineage(Track >> Stemma):
        pass



    #===============================
    class Effect(CDOThing):
        pass
    class Scheme(CDOThing):
        pass
    class traces(Stemma >> Effect):
        pass
    class isAddressedBy(Effect >> Scheme):
        pass
    class hasStructure(Object >> Scheme):
        pass
    class demonstrates(Event >> Effect):
        pass
    class isCausal(Object >> Effect):
        pass

    #######################################
    class Concept(Subjective):
        pass

    class Term(CDOThing):
        pass
    class describedBy(Concept >> Term):
        pass
    
    class Notice(CDOThing):
        pass
    class isDocumentedIn(Term >> Notice):
        pass

    class Frame(CDOThing):
        pass
    class isFramedBy(Notice >> Frame):
        pass

    class Context(CDOThing):
        pass
    class isContextual(Frame >> Context):
        pass
    
    class contextualizes(Concept >> Object):
        pass

    class hasKnowledge(Concept >> Scheme):
        pass
    #===============================
    class Goal(CDOThing):
        pass
    class isAchieved(Event >> Goal):
        pass
    class defines(Concept >> Goal):
        pass



    #######################################
    class Action(Active):
        pass

    class Value(CDOThing):
        pass
    class processes(Action >> Value):
        pass

    class Payload(CDOThing):
        pass
    class constitutes(Value >> Payload):
        pass
                
    class Packet(CDOThing):
        pass
    class isTransmittedBy(Payload >> Packet):
        pass

    class Fact(CDOThing):
        pass
    rdfs.comment[Fact] = ["A Value is factual once a Packet's ACK (acknowledgement) message is received."]
    class isBasisFor(Packet >> Fact):
        pass

    class triggers(Action >> Event):
        pass
    #======================================
    class Method(CDOThing):
        pass
    class Reason(CDOThing):
        pass
    class instanceOf(Action >> Method):
        pass
    class isExpressedAs(Concept >> Method):
        pass
    class isJustifiedBy(Method >> Reason):
        pass
    class hasIntelligence(Action >> Reason):
        pass
    class hasCausality(Event >> Reason):
        pass

    #-----------------------------------------
    class Package(CDOThing):
        pass
    class formsBasisOf(Context >> Package):
        pass
    class hasValidity(Fact >> Package):
        pass
    class utlizes(Package >> Method):
        pass
    #======================================
    class Cause(CDOThing):
        pass
    class innitiates(Action  >> Cause):
        pass
    class isAffectedBy(Object >> Cause):
        pass
    

    #######################################
    class Data(CDOThing):
        pass
    class capturedAs (Data >> Object):
        pass
    class exchangedThrough(Data >> Action):
        pass
    class enteredAs(Data >> Event):
        pass
    class accessedBy(Data >> Concept):
        pass
