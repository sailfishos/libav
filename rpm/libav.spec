Name:           libav
Version:        11.8
Release:        0.0
Summary:        Libav video encoding and decoding library
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://libav.org
Source:         %{name}-%{version}.tar.gz
Patch0:         0001-Fix-linking-errors-when-VC1-parser-is-enabled-and-VC.patch
License:        LGPLv2+
BuildRequires:  pkgconfig(speex)
%ifarch i486
BuildRequires:  yasm
%endif

%description
Libav is a complete, cross-platform solution to decode, encode, record, convert and stream audio and video.

%package devel
Summary:        Development headers and libraries for libav
Requires:       %{name} = %{version}
Requires:       bzip2-devel

%description devel
Libav is a complete, cross-platform solution to decode, encode, record, convert and stream audio and video.

%package tools
Summary:        Libav tools package
Requires:       %{name} = %{version}

%description tools
Libav is a complete, cross-platform solution to decode, encode, record, convert and stream audio and video.

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build

./configure --prefix=/usr --libdir=%{_libdir} --disable-debug --enable-shared --enable-pic \
  --disable-static --disable-doc --disable-muxers --disable-demuxers --disable-protocols \
  --disable-indevs --disable-outdevs --disable-avdevice --disable-network \
  --disable-lsp --disable-hwaccels --disable-encoders --disable-decoders --disable-bsfs \
  --enable-protocol=file --enable-fft --enable-decoder=aac --enable-decoder=aac_latm \
  --enable-decoder=vorbis --enable-decoder=theora --enable-decoder=flac \
  --enable-encoder=aac --enable-demuxer=aac --enable-demuxer=avi --enable-demuxer=flac \
  --enable-demuxer=h264 --enable-demuxer=m4v --enable-demuxer=mov --enable-demuxer=ogg \
  --enable-demuxer=mpegts --enable-demuxer=mpegvideo --enable-demuxer=matroska \
  --enable-demuxer=wav --enable-decoder=h264 --enable-decoder=mpeg4 --enable-decoder=mp3 \
  --enable-demuxer=aiff --enable-demuxer=flv --enable-demuxer=mjpeg \
  --enable-decoder=pcm_u8 --enable-decoder=pcm_u32le --enable-decoder=pcm_u32be \
  --enable-decoder=pcm_u24le --enable-decoder=pcm_u24be --enable-decoder=pcm_u16le \
  --enable-decoder=pcm_u16be --enable-decoder=pcm_s8 --enable-decoder=pcm_s32le \
  --enable-decoder=pcm_s32be --enable-decoder=pcm_s24le --enable-decoder=pcm_s24be \
  --enable-decoder=pcm_s16le --enable-decoder=pcm_s16be --enable-decoder=pcm_f64le \
  --enable-decoder=pcm_f64be --enable-decoder=pcm_f32le --enable-decoder=pcm_f32be \
  --enable-demuxer=pcm_u32be --enable-demuxer=pcm_u32le --enable-demuxer=pcm_u8 \
  --enable-demuxer=pcm_alaw --enable-demuxer=pcm_f32be --enable-demuxer=pcm_f32le \
  --enable-demuxer=pcm_f64be --enable-demuxer=pcm_f64le --enable-demuxer=pcm_s16be \
  --enable-demuxer=pcm_s16le --enable-demuxer=pcm_s24be --enable-demuxer=pcm_s24le \
  --enable-demuxer=pcm_s32be --enable-demuxer=pcm_s32le --enable-demuxer=pcm_s8 \
  --enable-demuxer=pcm_u16be --enable-demuxer=pcm_u16le --enable-demuxer=pcm_u24be \
  --enable-demuxer=pcm_u24le --enable-decoder=mjpeg --enable-decoder=vp8 \
  --enable-libspeex --enable-decoder=opus


make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/avconv/*.avpreset
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/libavcodec/*.h
%{_includedir}/libavfilter/*.h
%{_includedir}/libavformat/*.h
%{_includedir}/libavutil/*.h
%{_includedir}/libswscale/*.h
%{_includedir}/libavresample/*.h
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/avprobe
%{_bindir}/avconv
