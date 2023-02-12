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
        4,1,13,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,2,1,2,1,
        3,1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,9,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,81,8,6,10,6,12,6,
        84,9,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,86,0,14,1,0,0,0,2,19,
        1,0,0,0,4,30,1,0,0,0,6,41,1,0,0,0,8,50,1,0,0,0,10,52,1,0,0,0,12,
        71,1,0,0,0,14,15,3,2,1,0,15,16,3,4,2,0,16,17,3,6,3,0,17,18,5,0,0,
        1,18,1,1,0,0,0,19,20,5,1,0,0,20,25,5,12,0,0,21,22,5,7,0,0,22,24,
        5,12,0,0,23,21,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,
        26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,6,0,0,29,3,1,0,0,0,30,31,5,2,
        0,0,31,36,5,12,0,0,32,33,5,7,0,0,33,35,5,12,0,0,34,32,1,0,0,0,35,
        38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,
        0,39,40,5,6,0,0,40,5,1,0,0,0,41,45,3,8,4,0,42,44,3,8,4,0,43,42,1,
        0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,
        45,1,0,0,0,48,51,3,10,5,0,49,51,3,12,6,0,50,48,1,0,0,0,50,49,1,0,
        0,0,51,9,1,0,0,0,52,53,5,12,0,0,53,54,5,9,0,0,54,55,5,12,0,0,55,
        56,5,10,0,0,56,57,5,5,0,0,57,58,5,11,0,0,58,59,5,4,0,0,59,66,5,12,
        0,0,60,61,5,8,0,0,61,62,5,11,0,0,62,63,5,4,0,0,63,65,5,12,0,0,64,
        60,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,
        0,68,66,1,0,0,0,69,70,5,6,0,0,70,11,1,0,0,0,71,72,5,12,0,0,72,73,
        5,5,0,0,73,74,5,11,0,0,74,75,5,4,0,0,75,82,5,12,0,0,76,77,5,8,0,
        0,77,78,5,11,0,0,78,79,5,4,0,0,79,81,5,12,0,0,80,76,1,0,0,0,81,84,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,
        85,86,5,6,0,0,86,13,1,0,0,0,6,25,36,45,50,66,82
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
    RULE_defactions = 2
    RULE_transitions = 3
    RULE_trans = 4
    RULE_transact = 5
    RULE_transnoact = 6

    ruleNames =  [ "program", "defstates", "defactions", "transitions", 
                   "trans", "transact", "transnoact" ]

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
            self.state = 14
            self.defstates()
            self.state = 15
            self.defactions()
            self.state = 16
            self.transitions()
            self.state = 17
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(gramParser.STATES)
            self.state = 20
            self.match(gramParser.ID)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 21
                self.match(gramParser.VIRG)
                self.state = 22
                self.match(gramParser.ID)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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
        self.enterRule(localctx, 4, self.RULE_defactions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(gramParser.ACTIONS)
            self.state = 31
            self.match(gramParser.ID)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 32
                self.match(gramParser.VIRG)
                self.state = 33
                self.match(gramParser.ID)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
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
        self.enterRule(localctx, 6, self.RULE_transitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.trans()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 42
                self.trans()
                self.state = 47
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
        self.enterRule(localctx, 8, self.RULE_trans)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.transact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
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
        self.enterRule(localctx, 10, self.RULE_transact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(gramParser.ID)
            self.state = 53
            self.match(gramParser.LCROCH)
            self.state = 54
            self.match(gramParser.ID)
            self.state = 55
            self.match(gramParser.RCROCH)
            self.state = 56
            self.match(gramParser.FLECHE)
            self.state = 57
            self.match(gramParser.INT)
            self.state = 58
            self.match(gramParser.DPOINT)
            self.state = 59
            self.match(gramParser.ID)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 60
                self.match(gramParser.PLUS)
                self.state = 61
                self.match(gramParser.INT)
                self.state = 62
                self.match(gramParser.DPOINT)
                self.state = 63
                self.match(gramParser.ID)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
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
        self.enterRule(localctx, 12, self.RULE_transnoact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(gramParser.ID)
            self.state = 72
            self.match(gramParser.FLECHE)
            self.state = 73
            self.match(gramParser.INT)
            self.state = 74
            self.match(gramParser.DPOINT)
            self.state = 75
            self.match(gramParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 76
                self.match(gramParser.PLUS)
                self.state = 77
                self.match(gramParser.INT)
                self.state = 78
                self.match(gramParser.DPOINT)
                self.state = 79
                self.match(gramParser.ID)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





