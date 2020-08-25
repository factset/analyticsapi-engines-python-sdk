import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.*;
import org.openapitools.codegen.utils.ProcessUtils;

import java.io.File;

public class CustomPythonClientCodegen extends PythonClientCodegen {
    
    @Override
    public void processOpts() {
        super.processOpts();

        supportingFiles.add(new SupportingFile("utility_api.mustache", packagePath() + File.separatorChar + "api", "utility_api.py"));

        supportingFiles.add(new SupportingFile("utility_api_doc.mustache", apiDocPath, "UtilityApi.md"));

        supportingFiles.add(new SupportingFile("stach_extensions.mustache", packagePath(), "stach_extensions.py"));
    }
}