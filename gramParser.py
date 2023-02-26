# Generated from gram.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,1,1,1,3,1,26,8,1,1,2,1,2,
        1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,3,1,3,1,4,1,4,1,4,1,4,
        5,4,58,8,4,10,4,12,4,61,9,4,1,4,1,4,1,5,1,5,5,5,67,8,5,10,5,12,5,
        70,9,5,1,6,1,6,3,6,74,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,5,7,88,8,7,10,7,12,7,91,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,104,8,8,10,8,12,8,107,9,8,1,8,1,8,1,8,0,0,
        9,0,2,4,6,8,10,12,14,16,0,0,109,0,18,1,0,0,0,2,25,1,0,0,0,4,27,1,
        0,0,0,6,38,1,0,0,0,8,53,1,0,0,0,10,64,1,0,0,0,12,73,1,0,0,0,14,75,
        1,0,0,0,16,94,1,0,0,0,18,19,3,2,1,0,19,20,3,8,4,0,20,21,3,10,5,0,
        21,22,5,0,0,1,22,1,1,0,0,0,23,26,3,6,3,0,24,26,3,4,2,0,25,23,1,0,
        0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,5,1,0,0,28,33,5,12,0,0,29,30,
        5,7,0,0,30,32,5,12,0,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,6,0,0,37,5,1,0,
        0,0,38,39,5,1,0,0,39,40,5,12,0,0,40,41,5,4,0,0,41,48,5,11,0,0,42,
        43,5,7,0,0,43,44,5,12,0,0,44,45,5,4,0,0,45,47,5,11,0,0,46,42,1,0,
        0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,
        1,0,0,0,51,52,5,6,0,0,52,7,1,0,0,0,53,54,5,2,0,0,54,59,5,12,0,0,
        55,56,5,7,0,0,56,58,5,12,0,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,
        0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,6,0,0,63,
        9,1,0,0,0,64,68,3,12,6,0,65,67,3,12,6,0,66,65,1,0,0,0,67,70,1,0,
        0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,11,1,0,0,0,70,68,1,0,0,0,71,74,
        3,14,7,0,72,74,3,16,8,0,73,71,1,0,0,0,73,72,1,0,0,0,74,13,1,0,0,
        0,75,76,5,12,0,0,76,77,5,9,0,0,77,78,5,12,0,0,78,79,5,10,0,0,79,
        80,5,5,0,0,80,81,5,11,0,0,81,82,5,4,0,0,82,89,5,12,0,0,83,84,5,8,
        0,0,84,85,5,11,0,0,85,86,5,4,0,0,86,88,5,12,0,0,87,83,1,0,0,0,88,
        91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,
        0,92,93,5,6,0,0,93,15,1,0,0,0,94,95,5,12,0,0,95,96,5,5,0,0,96,97,
        5,11,0,0,97,98,5,4,0,0,98,105,5,12,0,0,99,100,5,8,0,0,100,101,5,
        11,0,0,101,102,5,4,0,0,102,104,5,12,0,0,103,99,1,0,0,0,104,107,1,
        0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,
        0,0,0,108,109,5,6,0,0,109,17,1,0,0,0,8,25,33,48,59,68,73,89,105
    ]

class gramParser ( Parser ):

    grammarFileName = "gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'States'", "'Actions'", "'transition'", 
                     "':'", "'->'", "';'", "','", "'+'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "STATES", "ACTIONS", "TRANSITION", "DPOINT", 
                      "FLECHE", "SEMI", "VIRG", "PLUS", "LCROCH", "RCROCH", 
                      "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_defstates = 1
    RULE_statenorew = 2
    RULE_staterew = 3
    RULE_defactions = 4
    RULE_transitions = 5
    RULE_trans = 6
    RULE_transact = 7
    RULE_transnoact = 8

    ruleNames =  [ "program", "defstates", "statenorew", "staterew", "defactions", 
                   "transitions", "trans", "transact", "transnoact" ]

    EOF = Token.EOF
    STATES=1
    ACTIONS=2
    TRANSITION=3
    DPOINT=4
    FLECHE=5
    SEMI=6
    VIRG=7
    PLUS=8
    LCROCH=9
    RCROCH=10
    INT=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defstates(self):
            return self.getTypedRuleContext(gramParser.DefstatesContext,0)


        def defactions(self):
            return self.getTypedRuleContext(gramParser.DefactionsContext,0)


        def transitions(self):
            return self.getTypedRuleContext(gramParser.TransitionsContext,0)


        def EOF(self):
            return self.getToken(gramParser.EOF, 0)

        def getRuleIndex(self):
            return gramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = gramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.defstates()
            self.state = 19
            self.defactions()
            self.state = 20
            self.transitions()
            self.state = 21
            self.match(gramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefstatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staterew(self):
            return self.getTypedRuleContext(gramParser.StaterewContext,0)


        def statenorew(self):
            return self.getTypedRuleContext(gramParser.StatenorewContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_defstates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefstates" ):
                listener.enterDefstates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefstates" ):
                listener.exitDefstates(self)




    def defstates(self):

        localctx = gramParser.DefstatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_defstates)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.staterew()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.statenorew()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatenorewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATES(self):
            return self.getToken(gramParser.STATES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_statenorew

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatenorew" ):
                listener.enterStatenorew(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatenorew" ):
                listener.exitStatenorew(self)




    def statenorew(self):

        localctx = gramParser.StatenorewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statenorew)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(gramParser.STATES)
            self.state = 28
            self.match(gramParser.ID)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 29
                self.match(gramParser.VIRG)
                self.state = 30
                self.match(gramParser.ID)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaterewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATES(self):
            return self.getToken(gramParser.STATES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_staterew

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaterew" ):
                listener.enterStaterew(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaterew" ):
                listener.exitStaterew(self)




    def staterew(self):

        localctx = gramParser.StaterewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_staterew)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(gramParser.STATES)
            self.state = 39
            self.match(gramParser.ID)
            self.state = 40
            self.match(gramParser.DPOINT)
            self.state = 41
            self.match(gramParser.INT)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 42
                self.match(gramParser.VIRG)
                self.state = 43
                self.match(gramParser.ID)
                self.state = 44
                self.match(gramParser.DPOINT)
                self.state = 45
                self.match(gramParser.INT)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefactionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIONS(self):
            return self.getToken(gramParser.ACTIONS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_defactions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefactions" ):
                listener.enterDefactions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefactions" ):
                listener.exitDefactions(self)




    def defactions(self):

        localctx = gramParser.DefactionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defactions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(gramParser.ACTIONS)
            self.state = 54
            self.match(gramParser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 55
                self.match(gramParser.VIRG)
                self.state = 56
                self.match(gramParser.ID)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trans(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.TransContext)
            else:
                return self.getTypedRuleContext(gramParser.TransContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_transitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitions" ):
                listener.enterTransitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitions" ):
                listener.exitTransitions(self)




    def transitions(self):

        localctx = gramParser.TransitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.trans()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 65
                self.trans()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transact(self):
            return self.getTypedRuleContext(gramParser.TransactContext,0)


        def transnoact(self):
            return self.getTypedRuleContext(gramParser.TransnoactContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_trans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrans" ):
                listener.enterTrans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrans" ):
                listener.exitTrans(self)




    def trans(self):

        localctx = gramParser.TransContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_trans)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.transact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.transnoact()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def LCROCH(self):
            return self.getToken(gramParser.LCROCH, 0)

        def RCROCH(self):
            return self.getToken(gramParser.RCROCH, 0)

        def FLECHE(self):
            return self.getToken(gramParser.FLECHE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.PLUS)
            else:
                return self.getToken(gramParser.PLUS, i)

        def getRuleIndex(self):
            return gramParser.RULE_transact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransact" ):
                listener.enterTransact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransact" ):
                listener.exitTransact(self)




    def transact(self):

        localctx = gramParser.TransactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_transact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(gramParser.ID)
            self.state = 76
            self.match(gramParser.LCROCH)
            self.state = 77
            self.match(gramParser.ID)
            self.state = 78
            self.match(gramParser.RCROCH)
            self.state = 79
            self.match(gramParser.FLECHE)
            self.state = 80
            self.match(gramParser.INT)
            self.state = 81
            self.match(gramParser.DPOINT)
            self.state = 82
            self.match(gramParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 83
                self.match(gramParser.PLUS)
                self.state = 84
                self.match(gramParser.INT)
                self.state = 85
                self.match(gramParser.DPOINT)
                self.state = 86
                self.match(gramParser.ID)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransnoactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def FLECHE(self):
            return self.getToken(gramParser.FLECHE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.PLUS)
            else:
                return self.getToken(gramParser.PLUS, i)

        def getRuleIndex(self):
            return gramParser.RULE_transnoact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransnoact" ):
                listener.enterTransnoact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransnoact" ):
                listener.exitTransnoact(self)




    def transnoact(self):

        localctx = gramParser.TransnoactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_transnoact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(gramParser.ID)
            self.state = 95
            self.match(gramParser.FLECHE)
            self.state = 96
            self.match(gramParser.INT)
            self.state = 97
            self.match(gramParser.DPOINT)
            self.state = 98
            self.match(gramParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 99
                self.match(gramParser.PLUS)
                self.state = 100
                self.match(gramParser.INT)
                self.state = 101
                self.match(gramParser.DPOINT)
                self.state = 102
                self.match(gramParser.ID)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





