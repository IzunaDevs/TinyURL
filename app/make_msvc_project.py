"""
Makes TinyURL MSVC project files
for an standalone python application.
"""


def _write_file(filename, data):
    with open(filename, 'w') as of:
        of.write(data)


def generate_tinyurl_rc():
    info = """// Microsoft Visual C++ generated resource script.
//
#include \"resource.h\"

#define APSTUDIO_READONLY_SYMBOLS
/////////////////////////////////////////////////////////////////////////////
//
// Generated from the TEXTINCLUDE 2 resource.
//
#include \"winres.h\"

/////////////////////////////////////////////////////////////////////////////
#undef APSTUDIO_READONLY_SYMBOLS

/////////////////////////////////////////////////////////////////////////////
// English (United States) resources

#if !defined(AFX_RESOURCE_DLL) || defined(AFX_TARG_ENU)
LANGUAGE LANG_ENGLISH, SUBLANG_ENGLISH_US

#ifdef APSTUDIO_INVOKED
/////////////////////////////////////////////////////////////////////////////
//
// TEXTINCLUDE
//

1 TEXTINCLUDE 
BEGIN
    \"resource.h\\0\"
END

2 TEXTINCLUDE 
BEGIN
    \"#include \"\"winres.h\"\"\\r\\n\"
    \"\\0\"
END

3 TEXTINCLUDE 
BEGIN
    \"\\r\\n\"
    \"\\0\"
END

#endif    // APSTUDIO_INVOKED


/////////////////////////////////////////////////////////////////////////////
//
// Icon
//

// Icon with lowest ID value placed first to ensure application icon
// remains consistent on all systems.
IDI_MAINICON            ICON                    \"rocket.ico\"


/////////////////////////////////////////////////////////////////////////////
//
// RCDATA
//
IDR_RCDATA1            RCDATA                    \"__main__.py\"

#endif    // English (United States) resources
/////////////////////////////////////////////////////////////////////////////



#ifndef APSTUDIO_INVOKED
/////////////////////////////////////////////////////////////////////////////
//
// Generated from the TEXTINCLUDE 3 resource.
//


/////////////////////////////////////////////////////////////////////////////
#endif    // not APSTUDIO_INVOKED

"""
    with open('TinyURL.rc', 'w', encoding='utf-16-le') as of:
        of.write(info)


def generate_resource_h():
    info = """//{{NO_DEPENDENCIES}}
// Microsoft Visual C++ generated include file.
// Used by TinyURL.rc
//
#define IDI_MAINICON                    1
#define IDR_RCDATA1                     1

// Next default values for new objects
// 
#ifdef APSTUDIO_INVOKED
#ifndef APSTUDIO_READONLY_SYMBOLS
#define _APS_NEXT_RESOURCE_VALUE        103
#define _APS_NEXT_COMMAND_VALUE         40001
#define _APS_NEXT_CONTROL_VALUE         1001
#define _APS_NEXT_SYMED_VALUE           101
#endif
#endif
"""
    _write_file('resource.h', info)


def generate_tinyurl_sln():
    info = """
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio 14
VisualStudioVersion = 14.0.25420.1
MinimumVisualStudioVersion = 10.0.40219.1
Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "TinyURL", "TinyURL.vcxproj", "{D7B5BBF6-730B-4A05-BAA0-649E388D817B}"
EndProject
Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Stuff", "Stuff", "{83DB229F-BA8F-42B9-97CC-F19EBC4BD0D3}"
	ProjectSection(SolutionItems) = preProject
		make_tinyurl_c.py = make_tinyurl_c.py
	EndProjectSection
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Release|x64 = Release|x64
		Release|x86 = Release|x86
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{D7B5BBF6-730B-4A05-BAA0-649E388D817B}.Release|x64.ActiveCfg = Release|x64
		{D7B5BBF6-730B-4A05-BAA0-649E388D817B}.Release|x64.Build.0 = Release|x64
		{D7B5BBF6-730B-4A05-BAA0-649E388D817B}.Release|x86.ActiveCfg = Release|Win32
		{D7B5BBF6-730B-4A05-BAA0-649E388D817B}.Release|x86.Build.0 = Release|Win32
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
EndGlobal
"""
    _write_file('TinyURL.sln', info)


def generate_tinyurl_vcxproj():
    info = """<?xml version="1.0" encoding="utf-8"?>
<Project DefaultTargets="Build" ToolsVersion="15.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup Label="ProjectConfigurations">
    <ProjectConfiguration Include="Release|Win32">
      <Configuration>Release</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Release|x64">
      <Configuration>Release</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
  </ItemGroup>
  <PropertyGroup Label="Globals">
    <ProjectGuid>{D7B5BBF6-730B-4A05-BAA0-649E388D817B}</ProjectGuid>
    <Keyword>Win32Proj</Keyword>
    <RootNamespace>TinyURL</RootNamespace>
    <WindowsTargetPlatformVersion>10.0.15063.0</WindowsTargetPlatformVersion>
  </PropertyGroup>
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.Default.props" />
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|Win32'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v141</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v141</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.props" />
  <ImportGroup Label="ExtensionSettings">
  </ImportGroup>
  <ImportGroup Label="Shared">
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <PropertyGroup Label="UserMacros" />
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">
    <LinkIncremental>false</LinkIncremental>
    <LibraryPath>E:\Python360\libs\;$(LibraryPath)</LibraryPath>
    <GenerateManifest>false</GenerateManifest>
    <IntDir>$(Configuration)\intermediate\</IntDir>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <LinkIncremental>false</LinkIncremental>
    <LibraryPath>E:\Python361x64\libs\;$(LibraryPath)</LibraryPath>
    <GenerateManifest>false</GenerateManifest>
    <IntDir>$(Platform)\$(Configuration)\intermediate\</IntDir>
  </PropertyGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <PrecompiledHeader>NotUsing</PrecompiledHeader>
      <Optimization>Full</Optimization>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <PreprocessorDefinitions>WIN32;NDEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <SDLCheck>true</SDLCheck>
      <RuntimeLibrary>MultiThreaded</RuntimeLibrary>
      <DebugInformationFormat>None</DebugInformationFormat>
      <ExceptionHandling>false</ExceptionHandling>
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <EnableCOMDATFolding>true</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>false</GenerateDebugInformation>
      <AdditionalDependencies>E:\Python360\libs\python36.lib;%(AdditionalDependencies)</AdditionalDependencies>
      <RandomizedBaseAddress>false</RandomizedBaseAddress>
      <FixedBaseAddress>true</FixedBaseAddress>
      <LinkTimeCodeGeneration />
      <LinkErrorReporting>NoErrorReport</LinkErrorReporting>
    </Link>
    <PreBuildEvent>
      <Command>
      </Command>
    </PreBuildEvent>
    <PostBuildEvent>
      <Command>del /F /Q $(Configuration)\intermediate\</Command>
    </PostBuildEvent>
  </ItemDefinitionGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <PrecompiledHeader>NotUsing</PrecompiledHeader>
      <Optimization>Full</Optimization>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <PreprocessorDefinitions>NDEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <SDLCheck>true</SDLCheck>
      <DebugInformationFormat>None</DebugInformationFormat>
      <RuntimeLibrary>MultiThreaded</RuntimeLibrary>
      <ExceptionHandling>false</ExceptionHandling>
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <EnableCOMDATFolding>false</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>false</GenerateDebugInformation>
      <LinkTimeCodeGeneration />
      <RandomizedBaseAddress>false</RandomizedBaseAddress>
      <FixedBaseAddress>true</FixedBaseAddress>
      <LinkErrorReporting>NoErrorReport</LinkErrorReporting>
    </Link>
    <PostBuildEvent>
      <Command>del /F /Q $(Platform)\$(Configuration)\intermediate\TinyURL.tlog\
del /F /Q $(Platform)\$(Configuration)\intermediate\</Command>
    </PostBuildEvent>
  </ItemDefinitionGroup>
  <ItemGroup>
    <ClCompile Include="TinyURL.c">
      <AdditionalIncludeDirectories Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">E:\Python360\include</AdditionalIncludeDirectories>
      <DebugInformationFormat Condition="'$(Configuration)|$(Platform)'=='Release|x64'">None</DebugInformationFormat>
      <Optimization Condition="'$(Configuration)|$(Platform)'=='Release|x64'">Full</Optimization>
      <RuntimeLibrary Condition="'$(Configuration)|$(Platform)'=='Release|x64'">MultiThreaded</RuntimeLibrary>
      <AdditionalIncludeDirectories Condition="'$(Configuration)|$(Platform)'=='Release|x64'">E:\Python361x64\include</AdditionalIncludeDirectories>
    </ClCompile>
  </ItemGroup>
  <ItemGroup>
    <ClInclude Include="resource.h" />
  </ItemGroup>
  <ItemGroup>
    <ResourceCompile Include="TinyURL.rc" />
  </ItemGroup>
  <ItemGroup>
    <Image Include="rocket.ico" />
  </ItemGroup>
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.targets" />
  <ImportGroup Label="ExtensionTargets">
  </ImportGroup>
</Project>"""
    _write_file('TinyURL.vcxproj', info)


def generate_tinyurl_vcxproj_filters():
    info = """<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup>
    <Filter Include="Source Files">
      <UniqueIdentifier>{4FC737F1-C7A5-4376-A066-2A32D752A2FF}</UniqueIdentifier>
      <Extensions>cpp;c;cc;cxx;def;odl;idl;hpj;bat;asm;asmx</Extensions>
    </Filter>
    <Filter Include="Header Files">
      <UniqueIdentifier>{93995380-89BD-4b04-88EB-625FBE52EBFB}</UniqueIdentifier>
      <Extensions>h;hh;hpp;hxx;hm;inl;inc;xsd</Extensions>
    </Filter>
    <Filter Include="Resource Files">
      <UniqueIdentifier>{67DA6AB6-F800-4c08-8B7A-83BB121AAD01}</UniqueIdentifier>
      <Extensions>rc;ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe;resx;tiff;tif;png;wav;mfcribbon-ms</Extensions>
    </Filter>
  </ItemGroup>
  <ItemGroup>
    <ClCompile Include="TinyURL.c">
      <Filter>Source Files</Filter>
    </ClCompile>
  </ItemGroup>
  <ItemGroup>
    <ClInclude Include="resource.h">
      <Filter>Header Files</Filter>
    </ClInclude>
  </ItemGroup>
  <ItemGroup>
    <ResourceCompile Include="TinyURL.rc">
      <Filter>Resource Files</Filter>
    </ResourceCompile>
  </ItemGroup>
  <ItemGroup>
    <Image Include="rocket.ico">
      <Filter>Resource Files</Filter>
    </Image>
  </ItemGroup>
</Project>"""
    _write_file('TinyURL.vcxproj.filters', info)

def main():
    generate_tinyurl_rc()
    generate_resource_h()
    generate_tinyurl_sln()
    generate_tinyurl_vcxproj()
    generate_tinyurl_vcxproj_filters()

main()
