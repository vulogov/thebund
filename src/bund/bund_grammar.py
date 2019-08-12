bund_grammar="""
BundContexts:
  history*=HistoryElement?
  env*=EnvironmentElement?
  contexts*=Context?
;

HistoryElement:
  '[history'
    story*=HistoryElementKV
  ';;'
;

HistoryElementKV:
  name=ID 'is' he_val=BASETYPE
;

EnvironmentElement:
  '[env'
    envstatement += EnvStatement
  ';;'
;

EnvStatement:
  name=/\w+(\.\w+)*/ "is" type=EnvStatementType("[" param=BASETYPE "]")? ("as" real_name=ID)?
;

EnvStatementType:
  "module" | "python"
;

Context:
  name=ID 'is'
    statements*=Statement
  ';;'
;

Statement:
  DataBlock | CodeBlockDecl | InBlockDecl | OutBlockDecl | VarBlock
;

DataBlock:
  '[data'
    definitions+=DataDefinitions[/,|;|(\s)*|(\n)*/]
    codeblock=CodeBlock?
  ';;'
;

VarBlock:
  '[var'
    definitions+=DataDefinitions[/,|;|(\s)*|(\n)*/]
  ';;'
;

CodeBlockDecl:
  name=ID 'is' codeblock=CodeBlock
;

InBlockDecl:
  '[in'
    in_chan += ChannelDefs[/,|;|(\s)*|(\n)*/]
  ';;'
;

OutBlockDecl:
  '[out'
    out_chan += ChannelDefs[/,|;|(\s)*|(\n)*/]
  ';;'
;

ChannelDefs:
  btype=ChannelBlockType? name=ChannelName("[" attr=Data "]")? "is" type=ChannelType ("as" ch_name=ID)?
;

ChannelType:
  "file" | "tmpfile" | "pipe" | "list" | "queue" | "string"
;

ChannelBlockType:
  "block" | "text"
;

ChannelName:
  ID | STRING
;

ChannelAttrs:
  name=ID '<-' val=BASETYPE
;

DataDefinitions:
  PushAssignment | PullAssignment
;

PushAssignment:
  value=Data '->' name=ID
;

PullAssignment:
  name=ID '<-' value=Data
;

List:
  '[' value+=Data[','] ']'
;

KVData:
  name=ID '<-' value=Data
;

KV:
  '{' kvalue+=KVData[',']
  '}'
;

Data:
  BASETYPE | List | KV | CodeBlock | CodeBlockRef
;

CodeBlock:
  "(" words+=CodeWords ")"
;

CodeBlockRef:
  "&(" words+=CodeWords ")"
;

CodeWords:
  Data | CodeWord | CodeWordSpecial | CodeWordModifyer | CodeBlock | CodeBlockRef | CodeWordWReferenceOnModule | CodeExecute | CodeWordsMonad
;

CodeWordModifyer:
  '+' | '-' | '*' | '&' | '=' | '?' | '!' | '$' | '@' | '%' | '^' | '|'
;

CodeWordSpecial:
  '++' | '--' | '==' | '<=' | '=>' | '<' | '>' | '===' | '+++' | '---'
;

CodeWordReferenceOnModule:
    '->'
;


CodeWord:
  prefix=CodeWordModifyer? word=ID suffix=CodeWordModifyer? param=CurryParam?
;

CodeWordNoParam:
  prefix=CodeWordModifyer? word=ID suffix=CodeWordModifyer?
;

CodeWordWReferenceOnModule:
  module=ID CodeWordReferenceOnModule fun=ID
;


CurryParam:
  "@" param=Data
;

CodeWordsMonad:
  "#("
     words += CodeWordMonad
  ")" param=CurryParam?
;

CodeWordMonad:
  CodeWordNoParam | CodeWordSpecial | CodeWordModifyer
;

CodeExecute:
  "." name=ID?
;

Comment:
  /\/\*.*\*\/|\/\/.*$/
;
"""
