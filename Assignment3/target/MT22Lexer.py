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
        buf.write("\u0263\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\u00b2\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u00be\n\3\3\4\3\4\3\5\3\5\7\5\u00c4\n\5\f\5\16\5\u00c7")
        buf.write("\13\5\3\6\3\6\5\6\u00cb\n\6\3\6\6\6\u00ce\n\6\r\6\16\6")
        buf.write("\u00cf\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00db\n")
        buf.write("\7\3\b\3\b\3\b\7\b\u00e0\n\b\f\b\16\b\u00e3\13\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00fa\n\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u0100\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u0174\n\37\3\37\3")
        buf.write("\37\3 \3 \3 \3 \7 \u017c\n \f \16 \u017f\13 \3 \3 \3 ")
        buf.write("\3!\3!\3!\3!\7!\u0188\n!\f!\16!\u018b\13!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3F\3F\7F\u023d\nF\fF\16F\u0240\13F\3G\6G\u0243")
        buf.write("\nG\rG\16G\u0244\3G\3G\3H\3H\3H\3I\3I\3I\7I\u024f\nI\f")
        buf.write("I\16I\u0252\13I\3I\5I\u0255\nI\3I\3I\3J\3J\3J\7J\u025c")
        buf.write("\nJ\fJ\16J\u025f\13J\3J\3J\3J\3\u017d\2K\3\3\5\4\7\2\t")
        buf.write("\2\13\2\r\5\17\6\21\2\23\2\25\2\27\7\31\b\33\t\35\n\37")
        buf.write("\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67")
        buf.write("\279\30;\31=\32?\2A\2C\33E\34G\35I\36K\37M O!Q\"S#U$W")
        buf.write("%Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67")
        buf.write("}8\1779\u0081:\u0083;\u0085<\u0087=\u0089>\u008b?\u008d")
        buf.write("@\u008fA\u0091B\u0093C\3\2\16\3\2\63;\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\5\2\f\f$$^^\t\2))^^ddhhppttvv\3\2$$\4\2\f\f\17")
        buf.write("\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\3\f")
        buf.write("\f\2\u0278\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3")
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
        buf.write("\3\2\2\2\5\u00bd\3\2\2\2\7\u00bf\3\2\2\2\t\u00c1\3\2\2")
        buf.write("\2\13\u00c8\3\2\2\2\r\u00da\3\2\2\2\17\u00dc\3\2\2\2\21")
        buf.write("\u00e7\3\2\2\2\23\u00f9\3\2\2\2\25\u00ff\3\2\2\2\27\u0101")
        buf.write("\3\2\2\2\31\u0106\3\2\2\2\33\u010e\3\2\2\2\35\u0113\3")
        buf.write("\2\2\2\37\u0119\3\2\2\2!\u011f\3\2\2\2#\u0125\3\2\2\2")
        buf.write("%\u012c\3\2\2\2\'\u0130\3\2\2\2)\u0138\3\2\2\2+\u013c")
        buf.write("\3\2\2\2-\u0143\3\2\2\2/\u014c\3\2\2\2\61\u014f\3\2\2")
        buf.write("\2\63\u0158\3\2\2\2\65\u015b\3\2\2\2\67\u0160\3\2\2\2")
        buf.write("9\u0163\3\2\2\2;\u0169\3\2\2\2=\u0173\3\2\2\2?\u0177\3")
        buf.write("\2\2\2A\u0183\3\2\2\2C\u018c\3\2\2\2E\u018e\3\2\2\2G\u0190")
        buf.write("\3\2\2\2I\u0192\3\2\2\2K\u0194\3\2\2\2M\u0196\3\2\2\2")
        buf.write("O\u0198\3\2\2\2Q\u019b\3\2\2\2S\u019e\3\2\2\2U\u01a1\3")
        buf.write("\2\2\2W\u01a4\3\2\2\2Y\u01a6\3\2\2\2[\u01a9\3\2\2\2]\u01ab")
        buf.write("\3\2\2\2_\u01ae\3\2\2\2a\u01b1\3\2\2\2c\u01b3\3\2\2\2")
        buf.write("e\u01b5\3\2\2\2g\u01b7\3\2\2\2i\u01b9\3\2\2\2k\u01bb\3")
        buf.write("\2\2\2m\u01bd\3\2\2\2o\u01bf\3\2\2\2q\u01c1\3\2\2\2s\u01c3")
        buf.write("\3\2\2\2u\u01c5\3\2\2\2w\u01c7\3\2\2\2y\u01d3\3\2\2\2")
        buf.write("{\u01dd\3\2\2\2}\u01e9\3\2\2\2\177\u01f4\3\2\2\2\u0081")
        buf.write("\u0201\3\2\2\2\u0083\u020e\3\2\2\2\u0085\u021a\3\2\2\2")
        buf.write("\u0087\u0225\3\2\2\2\u0089\u022b\3\2\2\2\u008b\u023a\3")
        buf.write("\2\2\2\u008d\u0242\3\2\2\2\u008f\u0248\3\2\2\2\u0091\u024b")
        buf.write("\3\2\2\2\u0093\u0258\3\2\2\2\u0095\u00aa\7\62\2\2\u0096")
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
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b4\b\3\3\2\u00b4\u00be\3\2\2\2")
        buf.write("\u00b5\u00b6\5\7\4\2\u00b6\u00b7\5\13\6\2\u00b7\u00b8")
        buf.write("\b\3\4\2\u00b8\u00be\3\2\2\2\u00b9\u00ba\5\t\5\2\u00ba")
        buf.write("\u00bb\5\13\6\2\u00bb\u00bc\b\3\5\2\u00bc\u00be\3\2\2")
        buf.write("\2\u00bd\u00ab\3\2\2\2\u00bd\u00b5\3\2\2\2\u00bd\u00b9")
        buf.write("\3\2\2\2\u00be\6\3\2\2\2\u00bf\u00c0\5\3\2\2\u00c0\b\3")
        buf.write("\2\2\2\u00c1\u00c5\7\60\2\2\u00c2\u00c4\t\3\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\n\3\2\2\2\u00c7\u00c5\3\2\2")
        buf.write("\2\u00c8\u00ca\t\4\2\2\u00c9\u00cb\t\5\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc")
        buf.write("\u00ce\t\3\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\f\3\2\2")
        buf.write("\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7")
        buf.write("w\2\2\u00d4\u00db\7g\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00db")
        buf.write("\7g\2\2\u00da\u00d1\3\2\2\2\u00da\u00d5\3\2\2\2\u00db")
        buf.write("\16\3\2\2\2\u00dc\u00e1\7$\2\2\u00dd\u00e0\5\21\t\2\u00de")
        buf.write("\u00e0\5\23\n\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2")
        buf.write("\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e5\7$\2\2\u00e5\u00e6\b\b\6\2\u00e6\20\3\2\2\2\u00e7")
        buf.write("\u00e8\n\6\2\2\u00e8\22\3\2\2\2\u00e9\u00ea\7^\2\2\u00ea")
        buf.write("\u00fa\7$\2\2\u00eb\u00ec\7^\2\2\u00ec\u00fa\7d\2\2\u00ed")
        buf.write("\u00ee\7^\2\2\u00ee\u00fa\7h\2\2\u00ef\u00f0\7^\2\2\u00f0")
        buf.write("\u00fa\7t\2\2\u00f1\u00f2\7^\2\2\u00f2\u00fa\7p\2\2\u00f3")
        buf.write("\u00f4\7^\2\2\u00f4\u00fa\7v\2\2\u00f5\u00f6\7^\2\2\u00f6")
        buf.write("\u00fa\7)\2\2\u00f7\u00f8\7^\2\2\u00f8\u00fa\7^\2\2\u00f9")
        buf.write("\u00e9\3\2\2\2\u00f9\u00eb\3\2\2\2\u00f9\u00ed\3\2\2\2")
        buf.write("\u00f9\u00ef\3\2\2\2\u00f9\u00f1\3\2\2\2\u00f9\u00f3\3")
        buf.write("\2\2\2\u00f9\u00f5\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\24")
        buf.write("\3\2\2\2\u00fb\u00fc\7^\2\2\u00fc\u0100\n\7\2\2\u00fd")
        buf.write("\u00fe\7)\2\2\u00fe\u0100\n\b\2\2\u00ff\u00fb\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u0100\26\3\2\2\2\u0101\u0102\7c\2")
        buf.write("\2\u0102\u0103\7w\2\2\u0103\u0104\7v\2\2\u0104\u0105\7")
        buf.write("q\2\2\u0105\30\3\2\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7v\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7i\2\2\u010b\u010c\7g\2\2\u010c\u010d\7t\2\2\u010d\32")
        buf.write("\3\2\2\2\u010e\u010f\7x\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7k\2\2\u0111\u0112\7f\2\2\u0112\34\3\2\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7t\2\2\u0115\u0116\7t\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7{\2\2\u0118\36\3\2\2\2\u0119\u011a")
        buf.write("\7d\2\2\u011a\u011b\7t\2\2\u011b\u011c\7g\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7m\2\2\u011e \3\2\2\2\u011f\u0120")
        buf.write("\7h\2\2\u0120\u0121\7n\2\2\u0121\u0122\7q\2\2\u0122\u0123")
        buf.write("\7c\2\2\u0123\u0124\7v\2\2\u0124\"\3\2\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7g\2\2\u0127\u0128\7v\2\2\u0128\u0129")
        buf.write("\7w\2\2\u0129\u012a\7t\2\2\u012a\u012b\7p\2\2\u012b$\3")
        buf.write("\2\2\2\u012c\u012d\7q\2\2\u012d\u012e\7w\2\2\u012e\u012f")
        buf.write("\7v\2\2\u012f&\3\2\2\2\u0130\u0131\7d\2\2\u0131\u0132")
        buf.write("\7q\2\2\u0132\u0133\7q\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135\u0136\7c\2\2\u0136\u0137\7p\2\2\u0137(\3")
        buf.write("\2\2\2\u0138\u0139\7h\2\2\u0139\u013a\7q\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b*\3\2\2\2\u013c\u013d\7u\2\2\u013d\u013e")
        buf.write("\7v\2\2\u013e\u013f\7t\2\2\u013f\u0140\7k\2\2\u0140\u0141")
        buf.write("\7p\2\2\u0141\u0142\7i\2\2\u0142,\3\2\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7q\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7k\2\2\u0148\u0149\7p\2\2\u0149\u014a")
        buf.write("\7w\2\2\u014a\u014b\7g\2\2\u014b.\3\2\2\2\u014c\u014d")
        buf.write("\7f\2\2\u014d\u014e\7q\2\2\u014e\60\3\2\2\2\u014f\u0150")
        buf.write("\7h\2\2\u0150\u0151\7w\2\2\u0151\u0152\7p\2\2\u0152\u0153")
        buf.write("\7e\2\2\u0153\u0154\7v\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7p\2\2\u0157\62\3\2\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159\u015a\7h\2\2\u015a\64\3\2\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7n\2\2\u015d\u015e\7u\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015f\66\3\2\2\2\u0160\u0161\7k\2\2\u0161\u0162")
        buf.write("\7h\2\2\u01628\3\2\2\2\u0163\u0164\7y\2\2\u0164\u0165")
        buf.write("\7j\2\2\u0165\u0166\7k\2\2\u0166\u0167\7n\2\2\u0167\u0168")
        buf.write("\7g\2\2\u0168:\3\2\2\2\u0169\u016a\7k\2\2\u016a\u016b")
        buf.write("\7p\2\2\u016b\u016c\7j\2\2\u016c\u016d\7g\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e\u016f\7k\2\2\u016f\u0170\7v\2\2\u0170<\3")
        buf.write("\2\2\2\u0171\u0174\5? \2\u0172\u0174\5A!\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\b\37\7\2\u0176>\3\2\2\2\u0177\u0178\7\61\2\2\u0178")
        buf.write("\u0179\7,\2\2\u0179\u017d\3\2\2\2\u017a\u017c\13\2\2\2")
        buf.write("\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017e\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u0180\u0181\7,\2\2\u0181\u0182\7\61\2\2\u0182")
        buf.write("@\3\2\2\2\u0183\u0184\7\61\2\2\u0184\u0185\7\61\2\2\u0185")
        buf.write("\u0189\3\2\2\2\u0186\u0188\n\t\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3")
        buf.write("\2\2\2\u018aB\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d")
        buf.write("\7-\2\2\u018dD\3\2\2\2\u018e\u018f\7/\2\2\u018fF\3\2\2")
        buf.write("\2\u0190\u0191\7,\2\2\u0191H\3\2\2\2\u0192\u0193\7\61")
        buf.write("\2\2\u0193J\3\2\2\2\u0194\u0195\7\'\2\2\u0195L\3\2\2\2")
        buf.write("\u0196\u0197\7#\2\2\u0197N\3\2\2\2\u0198\u0199\7(\2\2")
        buf.write("\u0199\u019a\7(\2\2\u019aP\3\2\2\2\u019b\u019c\7~\2\2")
        buf.write("\u019c\u019d\7~\2\2\u019dR\3\2\2\2\u019e\u019f\7?\2\2")
        buf.write("\u019f\u01a0\7?\2\2\u01a0T\3\2\2\2\u01a1\u01a2\7#\2\2")
        buf.write("\u01a2\u01a3\7?\2\2\u01a3V\3\2\2\2\u01a4\u01a5\7>\2\2")
        buf.write("\u01a5X\3\2\2\2\u01a6\u01a7\7>\2\2\u01a7\u01a8\7?\2\2")
        buf.write("\u01a8Z\3\2\2\2\u01a9\u01aa\7@\2\2\u01aa\\\3\2\2\2\u01ab")
        buf.write("\u01ac\7@\2\2\u01ac\u01ad\7?\2\2\u01ad^\3\2\2\2\u01ae")
        buf.write("\u01af\7<\2\2\u01af\u01b0\7<\2\2\u01b0`\3\2\2\2\u01b1")
        buf.write("\u01b2\7*\2\2\u01b2b\3\2\2\2\u01b3\u01b4\7+\2\2\u01b4")
        buf.write("d\3\2\2\2\u01b5\u01b6\7]\2\2\u01b6f\3\2\2\2\u01b7\u01b8")
        buf.write("\7_\2\2\u01b8h\3\2\2\2\u01b9\u01ba\7\60\2\2\u01baj\3\2")
        buf.write("\2\2\u01bb\u01bc\7.\2\2\u01bcl\3\2\2\2\u01bd\u01be\7=")
        buf.write("\2\2\u01ben\3\2\2\2\u01bf\u01c0\7<\2\2\u01c0p\3\2\2\2")
        buf.write("\u01c1\u01c2\7}\2\2\u01c2r\3\2\2\2\u01c3\u01c4\7\177\2")
        buf.write("\2\u01c4t\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6v\3\2\2\2\u01c7")
        buf.write("\u01c8\7t\2\2\u01c8\u01c9\7g\2\2\u01c9\u01ca\7c\2\2\u01ca")
        buf.write("\u01cb\7f\2\2\u01cb\u01cc\7K\2\2\u01cc\u01cd\7p\2\2\u01cd")
        buf.write("\u01ce\7v\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0\7i\2\2\u01d0")
        buf.write("\u01d1\7g\2\2\u01d1\u01d2\7t\2\2\u01d2x\3\2\2\2\u01d3")
        buf.write("\u01d4\7t\2\2\u01d4\u01d5\7g\2\2\u01d5\u01d6\7c\2\2\u01d6")
        buf.write("\u01d7\7f\2\2\u01d7\u01d8\7H\2\2\u01d8\u01d9\7n\2\2\u01d9")
        buf.write("\u01da\7q\2\2\u01da\u01db\7c\2\2\u01db\u01dc\7v\2\2\u01dc")
        buf.write("z\3\2\2\2\u01dd\u01de\7t\2\2\u01de\u01df\7g\2\2\u01df")
        buf.write("\u01e0\7c\2\2\u01e0\u01e1\7f\2\2\u01e1\u01e2\7D\2\2\u01e2")
        buf.write("\u01e3\7q\2\2\u01e3\u01e4\7q\2\2\u01e4\u01e5\7n\2\2\u01e5")
        buf.write("\u01e6\7g\2\2\u01e6\u01e7\7c\2\2\u01e7\u01e8\7p\2\2\u01e8")
        buf.write("|\3\2\2\2\u01e9\u01ea\7t\2\2\u01ea\u01eb\7g\2\2\u01eb")
        buf.write("\u01ec\7c\2\2\u01ec\u01ed\7f\2\2\u01ed\u01ee\7U\2\2\u01ee")
        buf.write("\u01ef\7v\2\2\u01ef\u01f0\7t\2\2\u01f0\u01f1\7k\2\2\u01f1")
        buf.write("\u01f2\7p\2\2\u01f2\u01f3\7i\2\2\u01f3~\3\2\2\2\u01f4")
        buf.write("\u01f5\7r\2\2\u01f5\u01f6\7t\2\2\u01f6\u01f7\7k\2\2\u01f7")
        buf.write("\u01f8\7p\2\2\u01f8\u01f9\7v\2\2\u01f9\u01fa\7K\2\2\u01fa")
        buf.write("\u01fb\7p\2\2\u01fb\u01fc\7v\2\2\u01fc\u01fd\7g\2\2\u01fd")
        buf.write("\u01fe\7i\2\2\u01fe\u01ff\7g\2\2\u01ff\u0200\7t\2\2\u0200")
        buf.write("\u0080\3\2\2\2\u0201\u0202\7r\2\2\u0202\u0203\7t\2\2\u0203")
        buf.write("\u0204\7k\2\2\u0204\u0205\7p\2\2\u0205\u0206\7v\2\2\u0206")
        buf.write("\u0207\7D\2\2\u0207\u0208\7q\2\2\u0208\u0209\7q\2\2\u0209")
        buf.write("\u020a\7n\2\2\u020a\u020b\7g\2\2\u020b\u020c\7c\2\2\u020c")
        buf.write("\u020d\7p\2\2\u020d\u0082\3\2\2\2\u020e\u020f\7r\2\2\u020f")
        buf.write("\u0210\7t\2\2\u0210\u0211\7k\2\2\u0211\u0212\7p\2\2\u0212")
        buf.write("\u0213\7v\2\2\u0213\u0214\7U\2\2\u0214\u0215\7v\2\2\u0215")
        buf.write("\u0216\7t\2\2\u0216\u0217\7k\2\2\u0217\u0218\7p\2\2\u0218")
        buf.write("\u0219\7i\2\2\u0219\u0084\3\2\2\2\u021a\u021b\7y\2\2\u021b")
        buf.write("\u021c\7t\2\2\u021c\u021d\7k\2\2\u021d\u021e\7v\2\2\u021e")
        buf.write("\u021f\7g\2\2\u021f\u0220\7H\2\2\u0220\u0221\7n\2\2\u0221")
        buf.write("\u0222\7q\2\2\u0222\u0223\7c\2\2\u0223\u0224\7v\2\2\u0224")
        buf.write("\u0086\3\2\2\2\u0225\u0226\7u\2\2\u0226\u0227\7w\2\2\u0227")
        buf.write("\u0228\7r\2\2\u0228\u0229\7g\2\2\u0229\u022a\7t\2\2\u022a")
        buf.write("\u0088\3\2\2\2\u022b\u022c\7r\2\2\u022c\u022d\7t\2\2\u022d")
        buf.write("\u022e\7g\2\2\u022e\u022f\7x\2\2\u022f\u0230\7g\2\2\u0230")
        buf.write("\u0231\7p\2\2\u0231\u0232\7v\2\2\u0232\u0233\7F\2\2\u0233")
        buf.write("\u0234\7g\2\2\u0234\u0235\7h\2\2\u0235\u0236\7c\2\2\u0236")
        buf.write("\u0237\7w\2\2\u0237\u0238\7n\2\2\u0238\u0239\7v\2\2\u0239")
        buf.write("\u008a\3\2\2\2\u023a\u023e\t\n\2\2\u023b\u023d\t\13\2")
        buf.write("\2\u023c\u023b\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u008c\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0241\u0243\t\f\2\2\u0242\u0241\3\2\2\2")
        buf.write("\u0243\u0244\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245\3")
        buf.write("\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\bG\7\2\u0247\u008e")
        buf.write("\3\2\2\2\u0248\u0249\13\2\2\2\u0249\u024a\bH\b\2\u024a")
        buf.write("\u0090\3\2\2\2\u024b\u0250\7$\2\2\u024c\u024f\5\21\t\2")
        buf.write("\u024d\u024f\5\23\n\2\u024e\u024c\3\2\2\2\u024e\u024d")
        buf.write("\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2\u0250")
        buf.write("\u0251\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2")
        buf.write("\u0253\u0255\t\r\2\2\u0254\u0253\3\2\2\2\u0255\u0256\3")
        buf.write("\2\2\2\u0256\u0257\bI\t\2\u0257\u0092\3\2\2\2\u0258\u025d")
        buf.write("\7$\2\2\u0259\u025c\5\21\t\2\u025a\u025c\5\23\n\2\u025b")
        buf.write("\u0259\3\2\2\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2\2\2")
        buf.write("\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260\3")
        buf.write("\2\2\2\u025f\u025d\3\2\2\2\u0260\u0261\5\25\13\2\u0261")
        buf.write("\u0262\bJ\n\2\u0262\u0094\3\2\2\2\33\2\u009a\u00a1\u00a5")
        buf.write("\u00a9\u00b0\u00bd\u00c5\u00ca\u00cf\u00da\u00df\u00e1")
        buf.write("\u00f9\u00ff\u0173\u017d\u0189\u023e\u0244\u024e\u0250")
        buf.write("\u0254\u025b\u025d\13\3\2\2\3\3\3\3\3\4\3\3\5\3\b\6\b")
        buf.write("\2\2\3H\7\3I\b\3J\t")
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
     

        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

        if actionIndex == 3:
            self.text = '0' + self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	esc = '\n'
            	if self.text[-1] in esc:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	raise IllegalEscape(self.text[1:])

     


