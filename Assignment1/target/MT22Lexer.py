# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0261\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\7\2\u0099\n\2\f\2\16\2\u009c\13\2\3\2\3\2\6\2\u00a0")
        buf.write("\n\2\r\2\16\2\u00a1\7\2\u00a4\n\2\f\2\16\2\u00a7\13\2")
        buf.write("\3\2\5\2\u00aa\n\2\3\3\3\3\3\3\7\3\u00af\n\3\f\3\16\3")
        buf.write("\u00b2\13\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00ba\n\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\7\5\u00c2\n\5\f\5\16\5\u00c5\13\5")
        buf.write("\3\6\3\6\5\6\u00c9\n\6\3\6\6\6\u00cc\n\6\r\6\16\6\u00cd")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00d9\n\7\3\b")
        buf.write("\3\b\3\b\7\b\u00de\n\b\f\b\16\b\u00e1\13\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u00f8\n\n\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00fe\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\5\37\u0172\n\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \7 \u017a\n \f \16 \u017d\13 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\7!\u0186\n!\f!\16!\u0189\13!\3\"\3\"\3#\3#\3$")
        buf.write("\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+")
        buf.write("\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3F\3F\7F\u023b\nF\fF\16F\u023e\13F\3G\6G\u0241")
        buf.write("\nG\rG\16G\u0242\3G\3G\3H\3H\3H\3I\3I\3I\7I\u024d\nI\f")
        buf.write("I\16I\u0250\13I\3I\5I\u0253\nI\3I\3I\3J\3J\3J\7J\u025a")
        buf.write("\nJ\fJ\16J\u025d\13J\3J\3J\3J\3\u017b\2K\3\3\5\4\7\2\t")
        buf.write("\2\13\2\r\5\17\6\21\2\23\2\25\2\27\7\31\b\33\t\35\n\37")
        buf.write("\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67")
        buf.write("\279\30;\31=\32?\2A\2C\33E\34G\35I\36K\37M O!Q\"S#U$W")
        buf.write("%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67")
        buf.write("}8\1779\u0081:\u0083;\u0085<\u0087=\u0089>\u008b?\u008d")
        buf.write("@\u008fA\u0091B\u0093C\3\2\16\3\2\63;\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\5\2\f\f$$^^\t\2))^^ddhhppttvv\3\2$$\4\2\f\f\17")
        buf.write("\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\3\f")
        buf.write("\f\2\u0276\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2")
        buf.write("G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2")
        buf.write("\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u00a9")
        buf.write("\3\2\2\2\5\u00b9\3\2\2\2\7\u00bd\3\2\2\2\t\u00bf\3\2\2")
        buf.write("\2\13\u00c6\3\2\2\2\r\u00d8\3\2\2\2\17\u00da\3\2\2\2\21")
        buf.write("\u00e5\3\2\2\2\23\u00f7\3\2\2\2\25\u00fd\3\2\2\2\27\u00ff")
        buf.write("\3\2\2\2\31\u0104\3\2\2\2\33\u010c\3\2\2\2\35\u0111\3")
        buf.write("\2\2\2\37\u0117\3\2\2\2!\u011d\3\2\2\2#\u0123\3\2\2\2")
        buf.write("%\u012a\3\2\2\2\'\u012e\3\2\2\2)\u0136\3\2\2\2+\u013a")
        buf.write("\3\2\2\2-\u0141\3\2\2\2/\u014a\3\2\2\2\61\u014d\3\2\2")
        buf.write("\2\63\u0156\3\2\2\2\65\u0159\3\2\2\2\67\u015e\3\2\2\2")
        buf.write("9\u0161\3\2\2\2;\u0167\3\2\2\2=\u0171\3\2\2\2?\u0175\3")
        buf.write("\2\2\2A\u0181\3\2\2\2C\u018a\3\2\2\2E\u018c\3\2\2\2G\u018e")
        buf.write("\3\2\2\2I\u0190\3\2\2\2K\u0192\3\2\2\2M\u0194\3\2\2\2")
        buf.write("O\u0196\3\2\2\2Q\u0199\3\2\2\2S\u019c\3\2\2\2U\u019f\3")
        buf.write("\2\2\2W\u01a2\3\2\2\2Y\u01a4\3\2\2\2[\u01a7\3\2\2\2]\u01a9")
        buf.write("\3\2\2\2_\u01ac\3\2\2\2a\u01af\3\2\2\2c\u01b1\3\2\2\2")
        buf.write("e\u01b3\3\2\2\2g\u01b5\3\2\2\2i\u01b7\3\2\2\2k\u01b9\3")
        buf.write("\2\2\2m\u01bb\3\2\2\2o\u01bd\3\2\2\2q\u01bf\3\2\2\2s\u01c1")
        buf.write("\3\2\2\2u\u01c3\3\2\2\2w\u01c5\3\2\2\2y\u01d1\3\2\2\2")
        buf.write("{\u01db\3\2\2\2}\u01e7\3\2\2\2\177\u01f2\3\2\2\2\u0081")
        buf.write("\u01ff\3\2\2\2\u0083\u020c\3\2\2\2\u0085\u0218\3\2\2\2")
        buf.write("\u0087\u0223\3\2\2\2\u0089\u0229\3\2\2\2\u008b\u0238\3")
        buf.write("\2\2\2\u008d\u0240\3\2\2\2\u008f\u0246\3\2\2\2\u0091\u0249")
        buf.write("\3\2\2\2\u0093\u0256\3\2\2\2\u0095\u00aa\7\62\2\2\u0096")
        buf.write("\u009a\t\2\2\2\u0097\u0099\t\3\2\2\u0098\u0097\3\2\2\2")
        buf.write("\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u00a5\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f")
        buf.write("\7a\2\2\u009e\u00a0\t\3\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a4\3\2\2\2\u00a3\u009d\3\2\2\2\u00a4\u00a7\3")
        buf.write("\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00aa\b\2\2\2\u00a9")
        buf.write("\u0095\3\2\2\2\u00a9\u0096\3\2\2\2\u00aa\4\3\2\2\2\u00ab")
        buf.write("\u00ac\5\7\4\2\u00ac\u00b0\5\t\5\2\u00ad\u00af\5\13\6")
        buf.write("\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00ba\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b4\5\7\4\2\u00b4\u00b5\5\13\6")
        buf.write("\2\u00b5\u00ba\3\2\2\2\u00b6\u00b7\5\t\5\2\u00b7\u00b8")
        buf.write("\5\13\6\2\u00b8\u00ba\3\2\2\2\u00b9\u00ab\3\2\2\2\u00b9")
        buf.write("\u00b3\3\2\2\2\u00b9\u00b6\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\b\3\3\2\u00bc\6\3\2\2\2\u00bd\u00be\5\3\2")
        buf.write("\2\u00be\b\3\2\2\2\u00bf\u00c3\7\60\2\2\u00c0\u00c2\t")
        buf.write("\3\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\n\3\2\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c6\u00c8\t\4\2\2\u00c7\u00c9\t\5\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2")
        buf.write("\u00ca\u00cc\t\3\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\f")
        buf.write("\3\2\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7w\2\2\u00d2\u00d9\7g\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5")
        buf.write("\7c\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d9")
        buf.write("\7g\2\2\u00d8\u00cf\3\2\2\2\u00d8\u00d3\3\2\2\2\u00d9")
        buf.write("\16\3\2\2\2\u00da\u00df\7$\2\2\u00db\u00de\5\21\t\2\u00dc")
        buf.write("\u00de\5\23\n\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2")
        buf.write("\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2")
        buf.write("\u00e3\7$\2\2\u00e3\u00e4\b\b\4\2\u00e4\20\3\2\2\2\u00e5")
        buf.write("\u00e6\n\6\2\2\u00e6\22\3\2\2\2\u00e7\u00e8\7^\2\2\u00e8")
        buf.write("\u00f8\7$\2\2\u00e9\u00ea\7^\2\2\u00ea\u00f8\7d\2\2\u00eb")
        buf.write("\u00ec\7^\2\2\u00ec\u00f8\7h\2\2\u00ed\u00ee\7^\2\2\u00ee")
        buf.write("\u00f8\7t\2\2\u00ef\u00f0\7^\2\2\u00f0\u00f8\7p\2\2\u00f1")
        buf.write("\u00f2\7^\2\2\u00f2\u00f8\7v\2\2\u00f3\u00f4\7^\2\2\u00f4")
        buf.write("\u00f8\7)\2\2\u00f5\u00f6\7^\2\2\u00f6\u00f8\7^\2\2\u00f7")
        buf.write("\u00e7\3\2\2\2\u00f7\u00e9\3\2\2\2\u00f7\u00eb\3\2\2\2")
        buf.write("\u00f7\u00ed\3\2\2\2\u00f7\u00ef\3\2\2\2\u00f7\u00f1\3")
        buf.write("\2\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\24")
        buf.write("\3\2\2\2\u00f9\u00fa\7^\2\2\u00fa\u00fe\n\7\2\2\u00fb")
        buf.write("\u00fc\7)\2\2\u00fc\u00fe\n\b\2\2\u00fd\u00f9\3\2\2\2")
        buf.write("\u00fd\u00fb\3\2\2\2\u00fe\26\3\2\2\2\u00ff\u0100\7c\2")
        buf.write("\2\u0100\u0101\7w\2\2\u0101\u0102\7v\2\2\u0102\u0103\7")
        buf.write("q\2\2\u0103\30\3\2\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7v\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7i\2\2\u0109\u010a\7g\2\2\u010a\u010b\7t\2\2\u010b\32")
        buf.write("\3\2\2\2\u010c\u010d\7x\2\2\u010d\u010e\7q\2\2\u010e\u010f")
        buf.write("\7k\2\2\u010f\u0110\7f\2\2\u0110\34\3\2\2\2\u0111\u0112")
        buf.write("\7c\2\2\u0112\u0113\7t\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115\u0116\7{\2\2\u0116\36\3\2\2\2\u0117\u0118")
        buf.write("\7d\2\2\u0118\u0119\7t\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7c\2\2\u011b\u011c\7m\2\2\u011c \3\2\2\2\u011d\u011e")
        buf.write("\7h\2\2\u011e\u011f\7n\2\2\u011f\u0120\7q\2\2\u0120\u0121")
        buf.write("\7c\2\2\u0121\u0122\7v\2\2\u0122\"\3\2\2\2\u0123\u0124")
        buf.write("\7t\2\2\u0124\u0125\7g\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7w\2\2\u0127\u0128\7t\2\2\u0128\u0129\7p\2\2\u0129$\3")
        buf.write("\2\2\2\u012a\u012b\7q\2\2\u012b\u012c\7w\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d&\3\2\2\2\u012e\u012f\7d\2\2\u012f\u0130")
        buf.write("\7q\2\2\u0130\u0131\7q\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133\u0134\7c\2\2\u0134\u0135\7p\2\2\u0135(\3")
        buf.write("\2\2\2\u0136\u0137\7h\2\2\u0137\u0138\7q\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139*\3\2\2\2\u013a\u013b\7u\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7t\2\2\u013d\u013e\7k\2\2\u013e\u013f")
        buf.write("\7p\2\2\u013f\u0140\7i\2\2\u0140,\3\2\2\2\u0141\u0142")
        buf.write("\7e\2\2\u0142\u0143\7q\2\2\u0143\u0144\7p\2\2\u0144\u0145")
        buf.write("\7v\2\2\u0145\u0146\7k\2\2\u0146\u0147\7p\2\2\u0147\u0148")
        buf.write("\7w\2\2\u0148\u0149\7g\2\2\u0149.\3\2\2\2\u014a\u014b")
        buf.write("\7f\2\2\u014b\u014c\7q\2\2\u014c\60\3\2\2\2\u014d\u014e")
        buf.write("\7h\2\2\u014e\u014f\7w\2\2\u014f\u0150\7p\2\2\u0150\u0151")
        buf.write("\7e\2\2\u0151\u0152\7v\2\2\u0152\u0153\7k\2\2\u0153\u0154")
        buf.write("\7q\2\2\u0154\u0155\7p\2\2\u0155\62\3\2\2\2\u0156\u0157")
        buf.write("\7q\2\2\u0157\u0158\7h\2\2\u0158\64\3\2\2\2\u0159\u015a")
        buf.write("\7g\2\2\u015a\u015b\7n\2\2\u015b\u015c\7u\2\2\u015c\u015d")
        buf.write("\7g\2\2\u015d\66\3\2\2\2\u015e\u015f\7k\2\2\u015f\u0160")
        buf.write("\7h\2\2\u01608\3\2\2\2\u0161\u0162\7y\2\2\u0162\u0163")
        buf.write("\7j\2\2\u0163\u0164\7k\2\2\u0164\u0165\7n\2\2\u0165\u0166")
        buf.write("\7g\2\2\u0166:\3\2\2\2\u0167\u0168\7k\2\2\u0168\u0169")
        buf.write("\7p\2\2\u0169\u016a\7j\2\2\u016a\u016b\7g\2\2\u016b\u016c")
        buf.write("\7t\2\2\u016c\u016d\7k\2\2\u016d\u016e\7v\2\2\u016e<\3")
        buf.write("\2\2\2\u016f\u0172\5? \2\u0170\u0172\5A!\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0174\b\37\5\2\u0174>\3\2\2\2\u0175\u0176\7\61\2\2\u0176")
        buf.write("\u0177\7,\2\2\u0177\u017b\3\2\2\2\u0178\u017a\13\2\2\2")
        buf.write("\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\7,\2\2\u017f\u0180\7\61\2\2\u0180")
        buf.write("@\3\2\2\2\u0181\u0182\7\61\2\2\u0182\u0183\7\61\2\2\u0183")
        buf.write("\u0187\3\2\2\2\u0184\u0186\n\t\2\2\u0185\u0184\3\2\2\2")
        buf.write("\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3")
        buf.write("\2\2\2\u0188B\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b")
        buf.write("\7-\2\2\u018bD\3\2\2\2\u018c\u018d\7/\2\2\u018dF\3\2\2")
        buf.write("\2\u018e\u018f\7,\2\2\u018fH\3\2\2\2\u0190\u0191\7\61")
        buf.write("\2\2\u0191J\3\2\2\2\u0192\u0193\7\'\2\2\u0193L\3\2\2\2")
        buf.write("\u0194\u0195\7#\2\2\u0195N\3\2\2\2\u0196\u0197\7(\2\2")
        buf.write("\u0197\u0198\7(\2\2\u0198P\3\2\2\2\u0199\u019a\7~\2\2")
        buf.write("\u019a\u019b\7~\2\2\u019bR\3\2\2\2\u019c\u019d\7?\2\2")
        buf.write("\u019d\u019e\7?\2\2\u019eT\3\2\2\2\u019f\u01a0\7#\2\2")
        buf.write("\u01a0\u01a1\7?\2\2\u01a1V\3\2\2\2\u01a2\u01a3\7>\2\2")
        buf.write("\u01a3X\3\2\2\2\u01a4\u01a5\7>\2\2\u01a5\u01a6\7?\2\2")
        buf.write("\u01a6Z\3\2\2\2\u01a7\u01a8\7@\2\2\u01a8\\\3\2\2\2\u01a9")
        buf.write("\u01aa\7@\2\2\u01aa\u01ab\7?\2\2\u01ab^\3\2\2\2\u01ac")
        buf.write("\u01ad\7<\2\2\u01ad\u01ae\7<\2\2\u01ae`\3\2\2\2\u01af")
        buf.write("\u01b0\7*\2\2\u01b0b\3\2\2\2\u01b1\u01b2\7+\2\2\u01b2")
        buf.write("d\3\2\2\2\u01b3\u01b4\7]\2\2\u01b4f\3\2\2\2\u01b5\u01b6")
        buf.write("\7_\2\2\u01b6h\3\2\2\2\u01b7\u01b8\7\60\2\2\u01b8j\3\2")
        buf.write("\2\2\u01b9\u01ba\7.\2\2\u01bal\3\2\2\2\u01bb\u01bc\7=")
        buf.write("\2\2\u01bcn\3\2\2\2\u01bd\u01be\7<\2\2\u01bep\3\2\2\2")
        buf.write("\u01bf\u01c0\7}\2\2\u01c0r\3\2\2\2\u01c1\u01c2\7\177\2")
        buf.write("\2\u01c2t\3\2\2\2\u01c3\u01c4\7?\2\2\u01c4v\3\2\2\2\u01c5")
        buf.write("\u01c6\7t\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8\7c\2\2\u01c8")
        buf.write("\u01c9\7f\2\2\u01c9\u01ca\7K\2\2\u01ca\u01cb\7p\2\2\u01cb")
        buf.write("\u01cc\7v\2\2\u01cc\u01cd\7g\2\2\u01cd\u01ce\7i\2\2\u01ce")
        buf.write("\u01cf\7g\2\2\u01cf\u01d0\7t\2\2\u01d0x\3\2\2\2\u01d1")
        buf.write("\u01d2\7t\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4\7c\2\2\u01d4")
        buf.write("\u01d5\7f\2\2\u01d5\u01d6\7H\2\2\u01d6\u01d7\7n\2\2\u01d7")
        buf.write("\u01d8\7q\2\2\u01d8\u01d9\7c\2\2\u01d9\u01da\7v\2\2\u01da")
        buf.write("z\3\2\2\2\u01db\u01dc\7t\2\2\u01dc\u01dd\7g\2\2\u01dd")
        buf.write("\u01de\7c\2\2\u01de\u01df\7f\2\2\u01df\u01e0\7D\2\2\u01e0")
        buf.write("\u01e1\7q\2\2\u01e1\u01e2\7q\2\2\u01e2\u01e3\7n\2\2\u01e3")
        buf.write("\u01e4\7g\2\2\u01e4\u01e5\7c\2\2\u01e5\u01e6\7p\2\2\u01e6")
        buf.write("|\3\2\2\2\u01e7\u01e8\7t\2\2\u01e8\u01e9\7g\2\2\u01e9")
        buf.write("\u01ea\7c\2\2\u01ea\u01eb\7f\2\2\u01eb\u01ec\7U\2\2\u01ec")
        buf.write("\u01ed\7v\2\2\u01ed\u01ee\7t\2\2\u01ee\u01ef\7k\2\2\u01ef")
        buf.write("\u01f0\7p\2\2\u01f0\u01f1\7i\2\2\u01f1~\3\2\2\2\u01f2")
        buf.write("\u01f3\7r\2\2\u01f3\u01f4\7t\2\2\u01f4\u01f5\7k\2\2\u01f5")
        buf.write("\u01f6\7p\2\2\u01f6\u01f7\7v\2\2\u01f7\u01f8\7K\2\2\u01f8")
        buf.write("\u01f9\7p\2\2\u01f9\u01fa\7v\2\2\u01fa\u01fb\7g\2\2\u01fb")
        buf.write("\u01fc\7i\2\2\u01fc\u01fd\7g\2\2\u01fd\u01fe\7t\2\2\u01fe")
        buf.write("\u0080\3\2\2\2\u01ff\u0200\7r\2\2\u0200\u0201\7t\2\2\u0201")
        buf.write("\u0202\7k\2\2\u0202\u0203\7p\2\2\u0203\u0204\7v\2\2\u0204")
        buf.write("\u0205\7D\2\2\u0205\u0206\7q\2\2\u0206\u0207\7q\2\2\u0207")
        buf.write("\u0208\7n\2\2\u0208\u0209\7g\2\2\u0209\u020a\7c\2\2\u020a")
        buf.write("\u020b\7p\2\2\u020b\u0082\3\2\2\2\u020c\u020d\7r\2\2\u020d")
        buf.write("\u020e\7t\2\2\u020e\u020f\7k\2\2\u020f\u0210\7p\2\2\u0210")
        buf.write("\u0211\7v\2\2\u0211\u0212\7U\2\2\u0212\u0213\7v\2\2\u0213")
        buf.write("\u0214\7t\2\2\u0214\u0215\7k\2\2\u0215\u0216\7p\2\2\u0216")
        buf.write("\u0217\7i\2\2\u0217\u0084\3\2\2\2\u0218\u0219\7y\2\2\u0219")
        buf.write("\u021a\7t\2\2\u021a\u021b\7k\2\2\u021b\u021c\7v\2\2\u021c")
        buf.write("\u021d\7g\2\2\u021d\u021e\7H\2\2\u021e\u021f\7n\2\2\u021f")
        buf.write("\u0220\7q\2\2\u0220\u0221\7c\2\2\u0221\u0222\7v\2\2\u0222")
        buf.write("\u0086\3\2\2\2\u0223\u0224\7u\2\2\u0224\u0225\7w\2\2\u0225")
        buf.write("\u0226\7r\2\2\u0226\u0227\7g\2\2\u0227\u0228\7t\2\2\u0228")
        buf.write("\u0088\3\2\2\2\u0229\u022a\7r\2\2\u022a\u022b\7t\2\2\u022b")
        buf.write("\u022c\7g\2\2\u022c\u022d\7x\2\2\u022d\u022e\7g\2\2\u022e")
        buf.write("\u022f\7p\2\2\u022f\u0230\7v\2\2\u0230\u0231\7F\2\2\u0231")
        buf.write("\u0232\7g\2\2\u0232\u0233\7h\2\2\u0233\u0234\7c\2\2\u0234")
        buf.write("\u0235\7w\2\2\u0235\u0236\7n\2\2\u0236\u0237\7v\2\2\u0237")
        buf.write("\u008a\3\2\2\2\u0238\u023c\t\n\2\2\u0239\u023b\t\13\2")
        buf.write("\2\u023a\u0239\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u008c\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023f\u0241\t\f\2\2\u0240\u023f\3\2\2\2")
        buf.write("\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3")
        buf.write("\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245\bG\5\2\u0245\u008e")
        buf.write("\3\2\2\2\u0246\u0247\13\2\2\2\u0247\u0248\bH\6\2\u0248")
        buf.write("\u0090\3\2\2\2\u0249\u024e\7$\2\2\u024a\u024d\5\21\t\2")
        buf.write("\u024b\u024d\5\23\n\2\u024c\u024a\3\2\2\2\u024c\u024b")
        buf.write("\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2\u024e")
        buf.write("\u024f\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0251\u0253\t\r\2\2\u0252\u0251\3\2\2\2\u0253\u0254\3")
        buf.write("\2\2\2\u0254\u0255\bI\7\2\u0255\u0092\3\2\2\2\u0256\u025b")
        buf.write("\7$\2\2\u0257\u025a\5\21\t\2\u0258\u025a\5\23\n\2\u0259")
        buf.write("\u0257\3\2\2\2\u0259\u0258\3\2\2\2\u025a\u025d\3\2\2\2")
        buf.write("\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025e\3")
        buf.write("\2\2\2\u025d\u025b\3\2\2\2\u025e\u025f\5\25\13\2\u025f")
        buf.write("\u0260\bJ\b\2\u0260\u0094\3\2\2\2\33\2\u009a\u00a1\u00a5")
        buf.write("\u00a9\u00b0\u00b9\u00c3\u00c8\u00cd\u00d8\u00dd\u00df")
        buf.write("\u00f7\u00fd\u0171\u017b\u0187\u023c\u0242\u024c\u024e")
        buf.write("\u0252\u0259\u025b\t\3\2\2\3\3\3\3\b\4\b\2\2\3H\5\3I\6")
        buf.write("\3J\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLLIT = 3
    STRINGLIT = 4
    AUTO = 5
    INTEGER = 6
    VOID = 7
    ARRAY = 8
    BREAK = 9
    FLOAT = 10
    RETURN = 11
    OUT = 12
    BOOLEAN = 13
    FOR = 14
    STRING = 15
    CONTINUE = 16
    DO = 17
    FUNCTION = 18
    OF = 19
    ELSE = 20
    IF = 21
    WHILE = 22
    INHERIT = 23
    COMMENT = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    NOT = 30
    AND = 31
    OR = 32
    EQUAL = 33
    NOT_EQUAL = 34
    SMALLER = 35
    SMALLER_EQUAL = 36
    GREATER = 37
    GREATER_EQUAL = 38
    CONCAT = 39
    LB = 40
    RB = 41
    LS = 42
    RS = 43
    DOT = 44
    COMMA = 45
    SEMI = 46
    COLON = 47
    LP = 48
    RP = 49
    ASSIGN = 50
    READI = 51
    READF = 52
    READB = 53
    READS = 54
    PRINTI = 55
    PRINTB = 56
    PRINTS = 57
    WRITEF = 58
    SUPER = 59
    PREVENTDEFAULT = 60
    ID = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'integer'", "'void'", "'array'", "'break'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='", 
            "'readInteger'", "'readFloat'", "'readBoolean'", "'readString'", 
            "'printInteger'", "'printBoolean'", "'printString'", "'writeFloat'", 
            "'super'", "'preventDefault'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "AUTO", "INTEGER", 
            "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
            "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", 
            "IF", "WHILE", "INHERIT", "COMMENT", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "SMALLER", 
            "SMALLER_EQUAL", "GREATER", "GREATER_EQUAL", "CONCAT", "LB", 
            "RB", "LS", "RS", "DOT", "COMMA", "SEMI", "COLON", "LP", "RP", 
            "ASSIGN", "READI", "READF", "READB", "READS", "PRINTI", "PRINTB", 
            "PRINTS", "WRITEF", "SUPER", "PREVENTDEFAULT", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "INTPART", "DECPART", "EXPPART", 
                  "BOOLLIT", "STRINGLIT", "STRING_DB", "ESCAPE", "ILL_ESCAPE", 
                  "AUTO", "INTEGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
                  "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                  "COMMENT", "COMMENT_C", "COMMENT_C2plus", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "SMALLER", "SMALLER_EQUAL", "GREATER", "GREATER_EQUAL", 
                  "CONCAT", "LB", "RB", "LS", "RS", "DOT", "COMMA", "SEMI", 
                  "COLON", "LP", "RP", "ASSIGN", "READI", "READF", "READB", 
                  "READS", "PRINTI", "PRINTB", "PRINTS", "WRITEF", "SUPER", 
                  "PREVENTDEFAULT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTLIT_action 
            actions[1] = self.FLOATLIT_action 
            actions[6] = self.STRINGLIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	esc = '\n'
            	if self.text[-1] in esc:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(self.text[1:])

     


