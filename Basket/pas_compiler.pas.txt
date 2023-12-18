program CompilePascalFiles;

{$APPTYPE CONSOLE}

uses
  SysUtils, Process;

procedure CompilePascalFilesInDirectory(const Directory: string);
var
  SearchRec: TSearchRec;
  Process: TProcess;
begin
  if FindFirst(Directory + '\*.pas', faAnyFile, SearchRec) = 0 then
  begin
    repeat
      if (SearchRec.Name <> '.') and (SearchRec.Name <> '..') then
      begin
        Process := TProcess.Create(nil);
        try
          Process.Executable := 'fpc'; // Укажите путь к компилятору, если не добавлен в PATH
          Process.Parameters.Add(Directory + '\' + SearchRec.Name);
          Process.Execute;
        finally
          Process.Free;
        end;
      end;
    until FindNext(SearchRec) <> 0;
    FindClose(SearchRec);
  end;
end;

begin
  try
    CompilePascalFilesInDirectory(ExtractFilePath(ParamStr(0)));
    Writeln('Компиляция завершена');
  except
    on E: Exception do
      Writeln('Ошибка: ', E.Message);
  end;
end.
