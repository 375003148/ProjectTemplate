#
#  Be sure to run `pod spec lint EWLogin.podspec' to ensure this is a
#  valid spec and to remove all comments including this before submitting the spec.
#
#  To learn more about Podspec attributes see https://guides.cocoapods.org/syntax/podspec.html
#  To see working Podspecs in the CocoaPods repo see https://github.com/CocoaPods/Specs/
#


Pod::Spec.new do |s|
    
  # =====================================
  # -------- Root specification ---------
  # =====================================
  
  # ---//Required//---
  # 名称
  s.name             = '${PODNAME}'
  # 版本
  s.version          = '0.1.0'
  # 简述
  s.summary          = '这是一个pod'
  # 作者和邮箱
  s.author           = { 'zzh' => '375003148@qq.com' }
  # 许可文件
  s.license          = { :type => 'MIT', :file => 'LICENSE' }
  # 项目主页地址，只支持HTTP和HTTPS地址，不支持ssh的地址
  s.homepage         = 'https://github.com/375003148'
  # 远程仓库的https地址
  s.source           = { :git => 'https://github.com/375003148/${PODNAME}.git', :tag => s.version.to_s }
  
  # ---//Optional//---
  # 详细介绍
  # s.description      = <<-DESC
  #                      这是一个pod
  #                      DESC
  # 截图URL
  # s.screenshots      = 'www.example.com/screenshots_1', 'www.example.com/screenshots_2'
  
  
  # ===========================================
  # --------------  Platform   ----------------
  # ===========================================
  
  # 指定平台和最低版本
  s.platform = :ios, '9.0'
  # 指定多平台时使用
  # spec.ios.deployment_target = '6.0'
  # spec.osx.deployment_target = '10.8'
  
  
  # ============================================
  # ------------  Build settings   -------------
  # ============================================
  
  # 依赖的三方库或者sub-specification
  # s.dependency 'AFNetworking', '~> 4.0'
  # 链接的系统framework
  # s.frameworks = 'UIKit', 'MapKit'
  # 链接的系统library库
  # s.libraries = 'xml2', 'static'
  
  # =============================================
  # -------------  File patterns   --------------
  # =============================================
  
  # 源文件
  s.source_files = '**/*.{h,m}'
  # s.source_files = '${PODNAME}/Classes/**/*'
  # 资源文件
  # s.resource_bundles = {
  #   '${PODNAME}' => ['${PODNAME}/Assets/*.png']
  # }
  # 拖入工程的三方framework
  # s.vendored_frameworks = 'MyFramework.framework', 'TheirFramework.framework'
  # 拖入工程的三方library
  # s.ios.vendored_library = 'Libraries/libProj4.a'
  
  
  # =========================================
  # --------------  Subspec   ---------------
  # =========================================
  # s.subspec 'Encryption' do |ss|
  #   ss.source_files = '${PODNAME}/Encryption/**/*.{h,m}'
  #   ss.dependency '${PODNAME}/Base64'
  # end

  # s.subspec 'Base64' do |ss|
  #   ss.source_files = '${PODNAME}/Base64/**/*.{h,m}'
  # end
  
end

